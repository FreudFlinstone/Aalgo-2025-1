import math

def F(n: int) -> int:
    if n == 1:  # Caso base
        return 2
    else:  # Caso recursivo
        return 2 * F(n - 1) + n ** 2


def F_formula(n: int) -> int:
    # Fórmula fechada usando math.pow para cálculo de potência
    return int(2 * (math.pow(2, n - 1)) + (n * (n + 1) * (2 * n + 1)) // 6)


def main():
    try:
        n = int(input('Digite um valor para n: '))
        if n < 1:
            print('Por favor, insira um número inteiro positivo.')
        else:
            resultado_recursivo = F(n)
            resultado_formula = F_formula(n)
            print(f'O resultado recursivo de F({n}) é: {resultado_recursivo}')
            print(f'O resultado usando a fórmula fechada de F({n}) é: {resultado_formula}')
    except ValueError:
        print('Entrada inválida! Por favor, insira um número inteiro.')


if __name__ == "__main__":
    main()
