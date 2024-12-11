import unittest
from numeroromano import converter_romano_para_inteiro

class TesteConversorRomano(unittest.TestCase):
    """
    Classe de testes para validar a conversão de números romanos em inteiros.
    """

    def test_conversoes_validas(self):
        """
        Testa conversões de números romanos válidos.
        """
        self.assertEqual(converter_romano_para_inteiro('I'), 1)
        self.assertEqual(converter_romano_para_inteiro('V'), 5)
        self.assertEqual(converter_romano_para_inteiro('II'), 2)
        self.assertEqual(converter_romano_para_inteiro('XXII'), 22)
        self.assertEqual(converter_romano_para_inteiro('IX'), 9)
        self.assertEqual(converter_romano_para_inteiro('XXIV'), 24)

    def test_conversoes_invalidas(self):
        """
        Testa entradas inválidas ou que violam regras do sistema numeral romano.
        """
        with self.assertRaises(ValueError):
            converter_romano_para_inteiro('IIII')

        with self.assertRaises(ValueError):
            converter_romano_para_inteiro('VV')

        with self.assertRaises(ValueError):
            converter_romano_para_inteiro('A')

if __name__ == "__main__":
    unittest.main()
