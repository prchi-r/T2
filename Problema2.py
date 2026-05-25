def sumar_posiciones_recursiva(arr, idx_actual, idx_final):
    if idx_actual > idx_final:
        return 0
    
    return arr[idx_actual] + sumar_posiciones_recursiva(arr, idx_actual + 1, idx_final)

def resolver_problema_2():
    try:
        n = int(input("Ingrese la cantidad de elementos de la lista: "))
        if n <= 0:
            print("La lista debe tener al menos 1 elemento.")
            return
            
        lista = []
        print("A continuación, ingrese los números de la lista:")
        for i in range(n):
            elemento = int(input(f"Elemento {i + 1}: "))
            lista.append(elemento)
            
        print(f"\nLista creada: {lista}")

        pi = int(input("Ingrese la posición inicial (PI): "))
        pf = int(input("Ingrese la posición final (PF): "))

        idx_inicial = pi - 1
        idx_final = pf - 1

        if idx_inicial < 0 or idx_final >= len(lista) or idx_inicial > idx_final:
            print("Error: Posiciones fuera de rango o inválidas.")
        else:
            resultado = sumar_posiciones_recursiva(lista, idx_inicial, idx_final)
            print(f"Resultado de la suma = {resultado}")
            
    except ValueError:
        print("Error: Por favor, ingrese únicamente números enteros.")
resolver_problema_2()