cont = 0
n = int(input('Digite um valor: '))
DD if n > 1:
for i in range(1, 11):
if n % i == 0:
cont += 1
if cont > 2:
else:
print(f'Não é primo, ele é divisivel {cont} vezes') print(f'É primo, ele é divisel apenas {cont} vezes') else:
print('Não é primo')
