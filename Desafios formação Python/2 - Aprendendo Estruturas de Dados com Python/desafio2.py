def elementos_comuns(lista1, lista2):
   
    # Converter as listas de strings para listas de inteiros
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))
    
    # Encontrar a interseção dos conjuntos
    comuns = set1.intersection(set2)
    
    # Retornar os elementos comuns como uma lista
    return list(comuns)

# Leitura das listas de entrada
lista1 = input().split()
lista2 = input().split()

# Verifica se todos os elementos das listas podem ser convertidos para inteiros
try:
    # Se a conversão falhar, uma exceção será levantada
    lista1 = list(map(int, lista1))
    lista2 = list(map(int, lista2))
    
    # Chama a função para encontrar os elementos comuns
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")

except ValueError:
    # Se ocorrer um ValueError, significa que a entrada não pode ser convertida para inteiro
    print("Entrada inválida.")
