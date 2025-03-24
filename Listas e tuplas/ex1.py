lista_de_compras = ['Sabão', 'Banana', 'Açúcar']

item = input("Digite o item que você quer verificar: ")

if item in lista_de_compras:
    print(f"O item {item} já está disponível na lista de compras")
else:
    print(f"O item {item} precisa ser comprado.")
print(lista_de_compras)

