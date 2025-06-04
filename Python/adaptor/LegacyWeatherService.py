from ThirdPartyWeatherService import ThirdPartyWeatherService

class LegacyWeatherService:
    def __init__(self, weather_api: ThirdPartyWeatherService):
        self.weather_api = weather_api

    def get_temperature(self, city: str, country: str) -> str:
        return self.weather_api.get_temperature(city, country)