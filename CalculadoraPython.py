import math

print("=" * 30)
print("        CALCULADORA")
print("=" * 30)
print("1 - Soma            (+)")
print("2 - Subtração       (-)")
print("3 - Multiplicação   (*)")
print("4 - Divisão         (/)")
print("5 - Raiz quadrada   (√)")
print("6 - Exponenciação   (^)")
print("7 - Seno            (sen)")
print("8 - Cosseno         (cos)")
print("=" * 30)

menu = int(input("Digite o número da operação: "))

if menu == 1:
    numeros1 = float(input("Escolha o primeiro número: "))
    numeros2 = float(input("Escolha o segundo número: "))
    print(numeros1 + numeros2)

elif menu == 2:
    numeros1 = float(input("Escolha o primeiro número: "))
    numeros2 = float(input("Escolha o segundo número: "))
    print(numeros1 - numeros2)

elif menu == 3:
    numeros1 = float(input("Escolha o primeiro número: "))
    numeros2 = float(input("Escolha o segundo número: "))
    print(numeros1 * numeros2)

elif menu == 4:
    numeros1 = float(input("Escolha o primeiro número: "))
    numeros2 = float(input("Escolha o segundo número: "))
    if numeros2 == 0:
        print("Não é possível dividir por zero.")
    else:
        print(numeros1 / numeros2)

elif menu == 5:
    numeros1 = float(input("Escolha o seu número (Raiz Quadrada): "))
    print(math.sqrt(numeros1))

elif menu == 6:
    numeros1 = float(input("Escolha a base: "))
    numeros2 = float(input("Escolha o expoente: "))
    print(numeros1 ** numeros2)

elif menu == 7:
    numeros1 = float(input("Escolha o ângulo em graus: "))
    print(math.sin(math.radians(numeros1)))

elif menu == 8:
    numeros1 = float(input("Escolha o ângulo em graus: "))
    print(math.cos(math.radians(numeros1)))

else:
    print("Opção inválida.")