class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature
        
    def to_fahrenheit(self):
        return 1.8 * self.temperature + 32
        
    @property
    def temperature(self):
        print('getting value')
        return self._temperature
        
    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError('temperature below -273 isnt possible')
        print('setting value')
        self._temperature = value