    # Напишите программу, которая получает целое число и возвращает его 
    # шестнадцатеричное строковое представление.
    # Функцию hex используйте для проверки своего результата.
import pytest


def hex_num(number: int) -> int:
   
    
    sixt = ''
    hexx = '0123456789ABCDEF'
    SIX = 16

    while number > 0:
        sixt = hexx[number % SIX] + sixt
        number = number // SIX

    return sixt 



def test_2():
    assert hex_num(123) == '7B', 'Test failed'

def test_3():
    assert hex_num(345) == '159', 'Test failed'

def test_4():
    assert hex_num(444) == '1BC', 'Test failed'

def test_5():
    assert hex_num(555) == '22B', 'Test failed'

def test_6():
    assert hex_num(777) == '309', 'Test failed'



if __name__ == "__main__":

    pytest.main()

    print(hex_num(123))