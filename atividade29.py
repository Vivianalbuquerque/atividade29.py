#Exercício Python 29: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
peso = []
for pessoa in range(5) :
    kg = int(input("digite seu peso."))
    peso.append(kg)
pesoord = sorted(peso)
print (pesoord[0], pesoord[4])