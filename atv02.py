# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.

num= int(input("digite um número: "))

def verificar_paridade(num):
    if num %2 == 0:
        return f"o número {num} é par"
    else:
        return f"o número {num} é impar"
 
resultado= verificar_paridade(num)
print(resultado)

verificar_paridade
