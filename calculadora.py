"""Operações aritméticas básicas."""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("O divisor não pode ser zero.")
    return a / b


if __name__ == "__main__":
    print("Soma de 8 e 2:", somar(8, 2))
    print("Divisão de 8 por 2:", dividir(8, 2))
