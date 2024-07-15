# No "TODO", abaixo: Crie a função 'soma_tupla' para receber uma tupla de números inteiros como argumento:

def soma_tupla(tupla):
    
    return sum(tupla)

if __name__ == "__main__":
    # Ler a entrada do usuário
    entrada = input()
    
    # Dividir a entrada em partes e converter cada parte em um número inteiro
    # map(int, entrada.split()) aplica a função int() a cada elemento da lista resultante de entrada.split()
    elementos = tuple(map(int, entrada.split()))
    
    # Calcular a soma dos elementos da tupla
    resultado = soma_tupla(elementos)
    
    # Exibir o resultado no formato especificado
    print(f"A soma dos elementos da tupla é: {resultado}")