from numeroromano import converter_romano_para_inteiro

if __name__ == "__main__":
    try:
        numero_romano = input("Digite um número romano: ")
        resultado = converter_romano_para_inteiro(numero_romano)
        print(f"O equivalente inteiro de {numero_romano} é {resultado}.")
    except ValueError as e:
        print(f"Erro: {e}")
