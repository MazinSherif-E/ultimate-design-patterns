from LegacyWeatherService import LegacyWeatherService
from ThirdPartyWeatherService import ThirdPartyWeatherService
from WeatherServiceAdaptee import WeatherServiceAdaptee

# Create the Third-Party Weather Service
third_party_service = ThirdPartyWeatherService()

# Wrap it in the Legacy Weather Service
legacy_service = LegacyWeatherService(third_party_service)

# Use the Adapter to make it compatible with the new system
adapter = WeatherServiceAdaptee(legacy_service)

# Fetch temperature using longitude & latitude
temperature = adapter.get_temperature(52.52, 13.405)  # Berlin (example)
print("Final Output:", temperature.get_temperature_data())