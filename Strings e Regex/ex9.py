import re

numero_cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX:")

padrao = r'(\d{3})\.\d{3}\.|d{3}-\d{2}'


if re.search(padrao, numero_cpf):
    print("O CPF está correto!")
else:
    print("O CPF está incorreto!")
