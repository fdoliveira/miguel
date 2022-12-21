print("Digite o primeiro numero:")
num1 = input()

print("Digite o primeiro numero:")
num2 = input()

if num1 == num2:
    print("Os números digitados são iguais", num1)
else:
    if num1 > num2:
        maior = num1
        menor = num2
    else:
        maior = num2
        menor = num1
    
    print("Os número maior é:", maior)
    print("Os número menor é:", menor)