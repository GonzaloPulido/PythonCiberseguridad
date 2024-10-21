def palindromo(palabra: str) -> bool:
    palabra = palabra.lower()
    palabra_volteada = palabra[::-1]  
    if palabra == palabra_volteada:
        return True  
    return False


if __name__ == "__main__":
    pass
    palabra = input()


    palindromo(palabra)


