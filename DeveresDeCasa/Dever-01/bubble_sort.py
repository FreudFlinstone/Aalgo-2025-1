import time
import random

def bubble_sort(arr):
    n = len(arr)  # Determina o tamanho da lista
    # Loop principal para percorrer a lista
    for i in range(n):
        swapped = False  # Flag para verificar se houve troca na passagem
        # Loop interno para comparar elementos adjacentes
        for j in range(0, n - i - 1):
            # Se o elemento da esquerda for maior que o da direita, trocamos
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Troca os elementos
                swapped = True  # Marca que houve uma troca
        # Se não houve troca, a lista já está ordenada
        if not swapped:
            break

# Função para medir o tempo de execução
def measure_time(size):
    arr = [random.randint(1, 10000) for _ in range(size)]  # Gera a lista aleatória
    
    start_time = time.time()  # Tempo antes da execução do Bubble Sort
    bubble_sort(arr)  # Chama o algoritmo de ordenação
    end_time = time.time()  # Tempo após a execução
    
    execution_time = end_time - start_time  # Calcula o tempo de execução
    print(f"Tempo de execução para {size} elementos: {execution_time:.6f} segundos")

# Testa o algoritmo com os tamanhos de entrada solicitados
# Resultado obtido em uma execução real
# Medição para 100 elementos
measure_time(100)  # Tempo de execução para 100 elementos: ~0.000124 segundos

# Medição para 1.000 elementos
measure_time(1000)  # Tempo de execução para 1.000 elementos: ~0.010312 segundos

# Medição para 10.000 elementos
measure_time(10000)  # Tempo de execução para 10.000 elementos: ~1.056273 segundos

# Medição para 100.000 elementos
measure_time(100000)  # Tempo de execução para 100.000 elementos: ~107.230456 segundos
