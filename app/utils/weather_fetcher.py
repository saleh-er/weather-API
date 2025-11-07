import requests
from typing import Optional, Dict

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(api_key: str, city: str, units: str = "metric", lang: str = "fr") -> Optional[Dict]:
    """
    Récupère la météo actuelle depuis OpenWeatherMap.
    Retourne un dict formaté ou None en cas d'erreur.
    """
    if not api_key:
        raise ValueError("API key is required")

    params = {
        "q": city,
        "appid": api_key,
        "units": units,
        "lang": lang
    }

    resp = requests.get(BASE_URL, params=params, timeout=10)
    if resp.status_code != 200:
        return None

    data = resp.json()
    # Formatage simple et utile pour l'API
    result = {
        "city": data.get("name"),
        "country": data.get("sys", {}).get("country"),
        "temperature_c": data.get("main", {}).get("temp"),
        "feels_like_c": data.get("main", {}).get("feels_like"),
        "humidity": data.get("main", {}).get("humidity"),
        "pressure_hpa": data.get("main", {}).get("pressure"),
        "weather_main": data.get("weather")[0].get("main") if data.get("weather") else None,
        "weather_description": data.get("weather")[0].get("description") if data.get("weather") else None,
    }
    return result
