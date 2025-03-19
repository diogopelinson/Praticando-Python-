a = int(input("Informe os dias para a atividade A: "))
b = int(input("Informe os dias para a atividade B: "))
c = int(input("Informe os dias para a atividade C: "))
if a < 0 or b <0 or c <0:
    print("Erro: os dias nao podem ser negativos")
else:
    tempo_total = a+b+c
    print(f"O tempo total das atividades e de {tempo_total}")