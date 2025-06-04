from abc import ABC, abstractmethod
from TemperatureData import TemperatureData

class WeatherServiceAdapter(ABC):
    @abstractmethod
    def get_temperature(self, longitude: float, latitude: float) -> TemperatureData:
        pass