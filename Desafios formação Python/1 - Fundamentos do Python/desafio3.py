texto = input()

def conta_vogais(texto):
    # Passo 1: Definir um conjunto de vogais
    vogais = set('aeiouAEIOU')
    
    # Passo 2: Inicializar o contador
    contador = 0
    
    # Passo 3: Iterar sobre cada caractere na string de entrada
    for caractere in texto:
        # Passo 4: Verificar se o caractere é uma vogal
        if caractere in vogais:
            # Passo 5: Incrementar o contador
            contador += 1
            
    # Passo 6: Retornar o valor do contador
    return contador

# Chamar a função e armazenar o resultado
numero_de_vogais = conta_vogais(texto)

# Exemplo de uso:

print(f"O número de vogais na string '{texto}' é: {numero_de_vogais}")     # Deve retornar 3 (contagem das vogais 'e', 'o', 'o')
