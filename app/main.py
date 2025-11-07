import json
from flask import Flask, jsonify, request
from app.config import Config
from app.utils.weather_fetcher import fetch_weather
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(exist_ok=True)
LOG_FILE = DATA_DIR / "logs.json"

def init_app():
    app = Flask(__name__)

    @app.route("/weather", methods=["GET"])
    def weather():
        city = request.args.get("city", Config.DEFAULT_CITY)
        api_key = Config.OPENWEATHER_API_KEY
        try:
            data = fetch_weather(api_key, city)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

        if data is None:
            return jsonify({"error": "Impossible de récupérer la météo pour la ville demandée"}), 502

        # Ajout d'un champ timestamp
        data_with_meta = {"fetched_at": datetime.utcnow().isoformat() + "Z", **data}

        # Sauvegarde dans logs.json
        try:
            if LOG_FILE.exists():
                with open(LOG_FILE, "r", encoding="utf-8") as f:
                    logs = json.load(f)
            else:
                logs = []
        except json.JSONDecodeError:
            logs = []

        logs.append(data_with_meta)
        # garder uniquement les 200 dernières entrées (par ex.)
        logs = logs[-200:]
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(logs, f, ensure_ascii=False, indent=2)

        return jsonify(data_with_meta)

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"}), 200

    return app

if __name__ == "__main__":
    app = init_app()
    app.run(host="0.0.0.0", port=5000, debug=False)
