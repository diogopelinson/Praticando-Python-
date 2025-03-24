

def somar(a, b):
    soma = a + b
    return soma

"""-------------------------------------------------------"""


def cumprimentar (nome = "Visitante"):
    print(f"Olá, {nome}!")

cumprimentar() #Saída: Olá, Visitante!

cumprimentar("Jhonathan") #Saída: Olá, Jhonathan

"""-------------------------------------------------------"""

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial (n-1)

print(fatorial(5)) # 5 x 4 x 3 x 2 x 1

"""-------------------------------------------------------"""

#Sintaxe lambda argumentos: expressão

soma = lambda a, b: a + b
print(soma(3, 5)) #Saída 8

"""-------------------------------------------------------"""

def multiplicador(n): # Função externa
    def multiplica(x): # Closure
        return x * n
    return multiplica # Retorna a função interna

triplo = multiplicador(3)
valor = triplo(5)
print(valor) # Saída: 15

"""-------------------------------------------------------"""

def big_mac ():
    print("Sanduiche big mac")

big_mac()


def fazer_big_mac(nome):
    print(f"Sanduiche big mac - {nome} ")

fazer_big_mac("Diogo")
fazer_big_mac("Jorlan")
fazer_big_mac("Adriana")


def fazer_batata(tamanho):
     print(f"Batata - {tamanho}")


def preparar_refrigerante(tipo,tamanho):
     print(f"{tipo} - {tamanho}")

def fazer_combo_completo(nome,tamanho_batata,tipo_refri,tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri, tamanho_refri)


fazer_combo_completo("Diogo", "Grande", "Coca", "Grande")



def soma_numeros(num1, num2):
    return num1 + num2

resultado = soma_numeros(15,20)
print(resultado)

def maior_numero(lista_numeros):
    lista_numeros.sort()
    lista_numeros.reverse()
    maior_numero = lista_numeros[0]
    return maior_numero


resultado = maior_numero([111, 232323, 334343545, 1221, 333, 111, 1, 2934])
print(resultado)




"""-------------------------------------------------------"""


def idades(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento

ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = idades(ano_nascimento, ano_atual)
print(f"A idade é {idade} anos")
