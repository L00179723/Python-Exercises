def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

kelvin_values = [273, 280, 290, 300, 310, 320, 330, 340, 350, 360]

for k in kelvin_values:
    celsius = kelvin_to_celsius(k)
    fahrenheit = kelvin_to_fahrenheit(k)
    print(f"{k} Kelvin is {celsius:.2f} Celsius and {fahrenheit:.2f} Fahrenheit")
