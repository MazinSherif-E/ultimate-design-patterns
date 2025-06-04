from WeatherServiceAdapter import WeatherServiceAdapter
from LegacyWeatherService import LegacyWeatherService
from TemperatureData import TemperatureData

class WeatherServiceAdaptee(WeatherServiceAdapter):
    def __init__(self, legacy_weather_service: LegacyWeatherService):
        self.legacy_weather_service = legacy_weather_service

    def get_temperature(self, longitude: float, latitude: float) -> TemperatureData:
        city = self.get_city_of(longitude, latitude)
        country = self.get_country_of(longitude, latitude)
        xml_data = self.legacy_weather_service.get_temperature(city, country)
        return self.convert_xml_to_json(xml_data)

    def convert_xml_to_json(self, xml_data: str) -> TemperatureData:
        print("Converting XML to JSON...")
        return TemperatureData("Converted Data from XML into JSON")

    def get_city_of(self, longitude: float, latitude: float) -> str:
        print(f"Extracting city for longitude: {longitude} and latitude: {latitude}")
        return "City"

    def get_country_of(self, longitude: float, latitude: float) -> str:
        print(f"Extracting country for longitude: {longitude} and latitude: {latitude}")
        return "Country"