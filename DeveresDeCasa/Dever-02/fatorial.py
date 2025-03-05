# Função recursiva para calcular o fatorial
def fatorial(n):
    # Caso base: o fatorial de 0 ou 1 é 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n * fatorial de n-1
    else:
        return n * fatorial(n - 1)

# Leitura do número inteiro
n = int(input("Digite um número inteiro: "))

# Verificando se o número é negativo, pois fatorial não existe para números negativos
if n < 0:
    print("O fatorial não existe para números negativos.")
else:
    # Chamando a função fatorial e imprimindo o resultado
    resultado = fatorial(n)
    print(f"O fatorial de {n} é {resultado}.")
