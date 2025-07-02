def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Erro: Não é possível calcular raiz quadrada de número negativo!"
    return x ** 0.5

print("Calculadora Simples")
print("Selecione a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potência")
print("6 - Raiz Quadrada")

while True:
    escolha = input("\nDigite o número da operação (ou 'q' para sair): ")
    
    if escolha == 'q':
        print("Obrigado por usar a calculadora!")
        break
        
    if escolha in ('1', '2', '3', '4', '5'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if escolha == '1':
            print(f"Resultado: {num1} + {num2} = {add(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {num1} - {num2} = {subtract(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {num1} * {num2} = {multiply(num1, num2)}")
        elif escolha == '4':
            print(f"Resultado: {num1} / {num2} = {divide(num1, num2)}")
        elif escolha == '5':
            print(f"Resultado: {num1} ^ {num2} = {power(num1, num2)}")
            
    elif escolha == '6':
        num = float(input("Digite o número para calcular a raiz quadrada: "))
        print(f"Resultado: √{num} = {square_root(num)}")
        
    else:
        print("Opção inválida!")