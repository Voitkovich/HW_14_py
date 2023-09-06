    # Напишите программу, которая получает целое число и возвращает его 
    # шестнадцатеричное строковое представление.
    # Функцию hex используйте для проверки своего результата.

def hex_num(number: int) -> int:
    """
    >>> hex_num(123)
    '7B'

    >>> hex_num(345)
    '159'

    >>> hex_num(444)
    '1BC'

    >>> hex_num(555)
    '22B'

    >>> hex_num(777)
    '309'

    """
    
    sixt = ''
    hexx = '0123456789ABCDEF'
    SIX = 16

    while number > 0:
        sixt = hexx[number % SIX] + sixt
        number = number // SIX

    return sixt 


if __name__ == "__main__":
    import doctest
    
    doctest.testmod(verbose=True)
    print(hex_num(123))