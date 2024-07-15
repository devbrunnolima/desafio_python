numero = int(input())

#Verifique se o número é par ou ímpar e imprima o resultado:

def eh_par(numero):
    return numero % 2 == 0
    
    
if eh_par(numero):
    print(f"Par")
else:
    print(f"Ímpar")    