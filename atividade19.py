# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.
a = int(input("digite um valor"))
fatorial = 1
while a > 1:
    fatorial*=a
    a -=1
    print("o fatorial deu {}". format(fatorial))