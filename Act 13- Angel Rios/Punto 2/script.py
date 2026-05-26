#2. En un banco se procesan datos de las 
# cuentas corrientes de sus clientes. De 
# cada cuenta corriente se conoce: número 
# de cuenta y saldo actual. El ingreso de 
# datos debe finalizar al ingresar un valor 
# negativo en el número de cuenta. Se pide 
# confeccionar un programa que lea los datos 
# de las cuentas corrientes e informe:
#a) De cada cuenta: número de cuenta y 
# estado de la cuenta según su saldo, 
# sabiendo que:
#Estado de la cuenta:
#“Acreedor” si el saldo es > 0.
#“Deudor” si el saldo es < 0.
#“Nulo” si el saldo es = 0.
#b) La suma total de los saldos acreedores.

sumaacreedores=0

numero=int(input("Ingrese número de cuenta: "))

while numero>=0:
    saldo=float(input("Ingrese saldo actual: "))

    if saldo>0:
        print("Cuenta:", numero, "Estado: Acreedor")
        sumaacreedores=sumaacreedores+saldo
    else:
        if saldo<0:
            print("Cuenta:", numero, "Estado: Deudor")
        else:
            print("Cuenta:", numero, "Estado: Nulo")

    numero=int(input("Ingrese número de cuenta: "))

print("Suma total de saldos acreedores:", sumaacreedores)

