# Given list of temperatures
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Extracting all the temperatures above 100
temperatures_above_100 = [temp for temp in temperatures if temp > 100]

# Displaying the extracted temperatures
print(temperatures_above_100)
