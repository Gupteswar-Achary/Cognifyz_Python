def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)


def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)


def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'C' and to_unit == 'F':
        return celsius_to_fahrenheit(value)
    elif from_unit == 'F' and to_unit == 'C':
        return fahrenheit_to_celsius(value)
    elif from_unit == 'C' and to_unit == 'K':
        return celsius_to_kelvin(value)
    elif from_unit == 'K' and to_unit == 'C':
        return kelvin_to_celsius(value)
    elif from_unit == 'F' and to_unit == 'K':
        return fahrenheit_to_kelvin(value)
    elif from_unit == 'K' and to_unit == 'F':
        return kelvin_to_fahrenheit(value)
    else:
        return None


def main():
    print("Temperature Converter")
    value = float(input("Enter the temperature value: "))
    from_unit = input("Enter the unit of the input temperature (C, F, K): ").upper()
    to_unit = input("Enter the unit to convert to (C, F, K): ").upper()

    converted_value = temperature_converter(value, from_unit, to_unit)

    if converted_value is not None:
        print(f"{value} {from_unit} is equal to {converted_value:.2f} {to_unit}")
    else:
        print("Invalid unit conversion.")


if __name__ == "__main__":
    main()
