limite = 3000
despesas_mensais = float(input("Digite o total de despesas do mes (R$): "))
if despesas_mensais > limite:
    print("Atencao! Voce ultrapassou seu limite de orcamento.")
else:
    print("Esta no limite!") 