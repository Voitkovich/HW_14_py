    # Напишите программу, которая получает целое число и возвращает его 
    # шестнадцатеричное строковое представление.
    # Функцию hex используйте для проверки своего результата.
import unittest


def hex_num(number: int) -> int:
   
    
    sixt = ''
    hexx = '0123456789ABCDEF'
    SIX = 16

    while number > 0:
        sixt = hexx[number % SIX] + sixt
        number = number // SIX

    return sixt 


class TestCaseNumbers(unittest.TestCase):
    def test_2(self):
        self.assertEqual(hex_num(123), '7B', msg='Test failed')

    def test_3(self):
        self.assertEqual(hex_num(345), '159', msg='Test failed')

    def test_4(self):
        self.assertEqual(hex_num(444), '1BC', msg='Test failed')

    def test_5(self):
        self.assertEqual(hex_num(555), '22B', msg='Test failed')

    def test_6(self):
        self.assertEqual(hex_num(777), '309', msg='Test failed')



if __name__ == "__main__":
  
    unittest.main()

    print(hex_num(123))