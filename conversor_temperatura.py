"""Conversões entre Celsius e Fahrenheit."""


def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    print("25 °C =", celsius_para_fahrenheit(25), "°F")
    print("77 °F =", fahrenheit_para_celsius(77), "°C")
