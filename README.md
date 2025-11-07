# 🌤️ Weather API

**Weather API** est un petit projet Python/Flask qui permet de récupérer la météo en temps réel pour une ville donnée grâce à l’API OpenWeatherMap.  

---

## 🔹 Fonctionnalités

- Récupération de la météo actuelle (température, humidité, pression, description) pour une ville donnée.
- Sauvegarde automatique des données récupérées dans un fichier `data/logs.json`.
- Endpoint `/health` pour vérifier que le service est actif.
- Projet structuré pour un usage professionnel et facile à versionner avec Git.

---

## 🛠️ Installation

1. Cloner le dépôt :
```bash
git clone https://github.com/tonusername/weather-api.git
cd weather-api

- Python 3.10+
- Clef API OpenWeatherMap (crée un fichier `.env` contenant `OPENWEATHER_API_KEY=ta_clef`)

```bash
python -m venv venv
source venv/bin/activate     # ou venv\Scripts\activate sur Windows
pip install -r requirements.txt
