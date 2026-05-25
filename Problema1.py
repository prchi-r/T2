import random

def min_max_multiplo3_recursivo(arr, idx=0, min_val=float('inf'), max_val=float('-inf')):
    if idx == len(arr):
        if min_val == float('inf'):
            return 0 
        return (min_val + max_val) / 2
    
    val = arr[idx]
    
    if val % 3 == 0:
        if val < min_val: min_val = val
        if val > max_val: max_val = val

    return min_max_multiplo3_recursivo(arr, idx + 1, min_val, max_val)

def resolver_problema_1():
    try:
        n = int(input("Ingrese el tamaño del arreglo: "))
        if n <= 0:
            print("El tamaño debe ser mayor a 0.")
            return

        arreglo = [random.randint(10, 9999) for _ in range(n)]
        print(f"Arreglo generado: {arreglo}")
        
        promedio = min_max_multiplo3_recursivo(arreglo)
        
        if promedio > 0:
            print(f"El promedio entre el máximo y mínimo múltiplo de 3 es: {promedio}")
        else:
            print("No se encontraron múltiplos de 3 en el arreglo.")
            
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
resolver_problema_1()
