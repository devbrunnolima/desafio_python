ano = int(input())
def verificador_ano_bissexto(ano):
     return (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)

#Verifique se o ano é bissexto utilizando uma estrutura de controle condicional, como if/else:


if verificador_ano_bissexto(ano):
  print(f"SIM")
  
else:
  print(f"NÃO")