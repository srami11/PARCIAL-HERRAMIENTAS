def main():
  while True:
      print("Menú:")
      print("1. Obtener representación en byte de un carácter")
      print("2. Obtener representación en byte de una palabra")
      print("0. Salir")

      opcion = input("Ingrese su opción (0-2): ")

      if opcion == '1':
          caracter = input("Ingrese un carácter: ")
          resultado = obtener_representacion_byte(caracter)
          print(f"Representación en byte de '{caracter}': {resultado}")
      elif opcion == '2':
          palabra = input("Ingrese una palabra: ")
          resultado = ' '.join(obtener_representacion_byte(c) for c in palabra)
          print(f"Representación en byte de '{palabra}': {resultado}")
      elif opcion == '0':
          print("Saliendo del programa")
          break
      else:
          print("Opción no válida. Ingrese un número del 0 al 2.")

if __name__ == "__main__":
  main()
