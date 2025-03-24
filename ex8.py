import re

nome = input("Digite seu nome para a validação: ")

if re.fullmatch(r'[A-Z][a-z]*', nome):
     print("Nome válido!")
else:
    print("Nome inválido!")