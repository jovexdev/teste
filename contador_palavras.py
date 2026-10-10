"""Conta palavras e caracteres em um texto."""


def contar_palavras(texto):
    return len(texto.split())


def contar_caracteres(texto, incluir_espacos=True):
    if incluir_espacos:
        return len(texto)
    return sum(1 for caractere in texto if not caractere.isspace())


if __name__ == "__main__":
    exemplo = "Este é um exemplo de texto."
    print("Palavras:", contar_palavras(exemplo))
    print("Caracteres sem espaços:", contar_caracteres(exemplo, incluir_espacos=False))
