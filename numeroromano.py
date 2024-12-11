def converter_romano_para_inteiro(numero_romano):
    """
    Converte um número romano para seu equivalente em número inteiro.

    :param numero_romano: String contendo o número em algarismos romanos.
    :return: O valor inteiro correspondente ao número romano.
    """
    tabela_valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    soma = 0
    ultimo_valor_direita = 0

    # Verifica se o número romano viola a regra de repetição
    if "IIII" in numero_romano or "VV" in numero_romano or "XXXX" in numero_romano \
            or "LL" in numero_romano or "CCCC" in numero_romano or "DD" in numero_romano \
            or "MMMM" in numero_romano:
        raise ValueError("Número romano inválido: repetição excessiva de caracteres.")

    # Itera pelos caracteres do número romano em ordem inversa
    for indice in reversed(range(len(numero_romano))):
        valor_atual = tabela_valores.get(numero_romano[indice], 0)

        if valor_atual == 0:
            raise ValueError(f"Caractere inválido encontrado: {numero_romano[indice]}")

        if valor_atual < ultimo_valor_direita:
            soma -= valor_atual
        else:
            soma += valor_atual

        ultimo_valor_direita = valor_atual

    return soma
