def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b


def potencia(a, b):
    return a ** b


def operacao_extra(a, b):
    resultado = a + b
    dobro = resultado * 2
    triplo = resultado * 3
    metade = resultado / 2
    quadrado = resultado ** 2
    cubo = resultado ** 3
    return resultado + dobro + triplo + metade + quadrado + cubo
