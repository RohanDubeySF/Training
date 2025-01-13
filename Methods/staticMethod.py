#Create a class TemperatureConverter that provides static methods to convert temperatures between Celsius and Fahrenheit. Implement the following static methods:celsius_to_fahrenheit(celsius): Converts a temperature from Celsius to Fahrenheit. fahrenheit_to_celsius(fahrenheit): Converts a temperature from Fahrenheit to Celsius.


class TemperatureConverter():
    @staticmethod
    def fahrenheit(celsius):
        return (celsius * 9/5) + 32
    @staticmethod
    def celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
celsius_temp = 25
fahrenheit_temp = TemperatureConverter.fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is {fahrenheit_temp}°F")  

fahrenheit_temp = 77
celsius_temp = TemperatureConverter.celsius(fahrenheit_temp)
print(f"{fahrenheit_temp}°F is {celsius_temp}°C")