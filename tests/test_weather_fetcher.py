import pytest
from app.utils.weather_fetcher import fetch_weather

def test_fetch_weather_no_key():
    with pytest.raises(ValueError):
        fetch_weather("", "Paris")

# Note: test réel contre l'API nécessite une clé et ferait un appel réseau.
# On se contente d'un test de non-régression simple.
