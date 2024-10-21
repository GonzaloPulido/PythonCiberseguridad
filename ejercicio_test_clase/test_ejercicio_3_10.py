from ejercicio_3_10 import palindromo

def test_palindromo():
    assert palindromo("reconocer") == True
    assert palindromo("arenera") == True
    assert palindromo("yeray") == False
    assert palindromo("ordenador") == False

    