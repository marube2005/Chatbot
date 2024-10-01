class Solution(object):
    def convertTemperature(self, Celsius):
        a = []
        Kelvin = Celsius + 273.15
        Fahrenheit = Celsius * 1.80 + 32.00
        a.append(Kelvin)
        a.append(Fahrenheit)
        return a

s1 = Solution()
print(s1.convertTemperature(23.45))   