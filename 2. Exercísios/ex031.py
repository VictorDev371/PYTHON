from time import sleep

distancia = float(input('Me informe a distancia da viajem em Km: '))
print("PROCESSANDO...")
sleep(1)
if distancia <= 200:
    print("O valor da passagem é: R${:.2f}".format(distancia*0.50))
else:
    print("O valor da passagem é: R${:.2f}".format(distancia*0.45))
