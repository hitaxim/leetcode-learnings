class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin, fahrenheit = celsius + 273.15, celsius * 1.80 + 32.00 
        return kelvin, fahrenheit
