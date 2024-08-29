#Programa que permita a un usuario tomar una decisión del tipo de pago a usar. Si la cuenta es menor a $150000 pago en efectivo. Si no, si es de $150000 hasta $300000 pago con el celular (dinero electrónico). Si es mayor a $300000 hasta $600000, pago con la tarjeta de débito. Todos los valores superiores a $6000000, pago con la tarjeta de crédito.
dinero = float(input("ingrese el dinero a pagar: "))

if dinero < 150000:
    print("realiza Pagas en efectivo")
elif dinero >= 150000 and dinero <= 300000:
    print("realiza Pago con el celular (dinero electronico)")
elif dinero >= 300000 and dinero <= 600000:
    print("realiza Pago con tarjeta de debito")
else:
    print("realiza pago con tarjeta de credito")