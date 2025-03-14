from typing import List, Any

def eh_palindromo(array: List[Any]) -> bool:
    # Caso base: se o array estiver vazio ou com um único elemento, é palíndromo
    if len(array) <= 1:
        return True
    
    # Verifica se os elementos das extremidades são iguais
    if array[0] != array[-1]:
        return False

    # Chamada recursiva excluindo os elementos das extremidades
    return eh_palindromo(array[1:-1])


# Testes
array1 = [0, 1, 2, 3, 2, 1, 0]
array2 = ["a", "b", "b", "a"]
array3 = ["a", "b", "c", "b", "a"]
array4 = ["a", "b", "c", "f", "b", "a"]

print(eh_palindromo(array1))  # True
print(eh_palindromo(array2))  # True
print(eh_palindromo(array3))  # True
print(eh_palindromo(array4))  # False
