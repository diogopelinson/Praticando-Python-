renda_mensal = int(input("Digite o valor da sua renda mensal: "))
parcela_desejada = int(input("Digite o valor da parcela desejada: "))
if renda_mensal >= 2000 and parcela_desejada <= 0.3 * renda_mensal:
    print("Emprestimo aprovado!")
elif renda_mensal <= 2000:
    print("Emprestimo negado: renda insuficiente.")
else:
    print("Emprestimo negado: parcela acima de 30% da renda.")