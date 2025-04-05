from time import sleep

numero = int(input("Me informe o número: "))
print("PROCESSANDO...")
sleep(1)
if numero%2==1:
    print("O seu número é impar!")
else: 
    print("O eu número é par!")