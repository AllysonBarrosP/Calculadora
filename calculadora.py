print("Calculadora Python - DSA")

def soma(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    return x / y
def exp(x,y):
    return x ** y

print("Escolha a opção:")
print("1 - Soma")
print("2 - Sub")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Exponencial")

escolha = input("Digite sua opção:")

num1 = int(input("Primeiro Número:"))
num2 = int(input("Segundo Número:"))

if escolha == '1':
    print(soma(num1, num2))
elif escolha == '2':
    print(sub(num1, num2))
elif escolha == '3':
    print(mult(num1, num2))
elif escolha == '4':
    print(div(num1, num2))
elif escolha == '5':
    print(exp(num1, num2))
else:
    print("Opção Inválida")

