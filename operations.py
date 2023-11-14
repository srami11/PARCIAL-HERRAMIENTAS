def obtener_representacion_byte(caracter):
  representacion_byte = ' '.join(format(b, '08b') for b in caracter.encode())
  return representacion_byte
def caracterabyte():
    caracter = 'A'
    valor_ascii = ord(caracter)
    representacion_byte = valor_ascii.to_bytes(1, byteorder='big')
    print(f"El carácter '{caracter}' en bytes es: {representacion_byte}")
def palabraAbyte(caracter):
palabra = input("Ingrese la palabra que desea cambiar a byte: ")
for letra in palabra:
    repreBits = format(ord(letra),'08b')
    print(f"{letra}: {repreBits}")
