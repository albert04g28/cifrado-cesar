
        import string

# Función para cifrar un texto con el cifrado César
def cifrar(texto, desplazamiento):
  # Inicializar el texto cifrado vacío
  texto_cifrado = ""
  # Recorrer cada caracter del texto
  for caracter in texto:
    # Si el caracter es una letra mayúscula
    if caracter in string.ascii_uppercase:
      # Obtener el número correspondiente al caracter (de 0 a 25)
      numero = ord(caracter) - ord("A")
      # Sumar el desplazamiento y aplicar el módulo 26 para obtener el nuevo número
      nuevo_numero = (numero + desplazamiento) % 26
      # Obtener el nuevo caracter correspondiente al nuevo número
      nuevo_caracter = chr(nuevo_numero + ord("A"))
      # Añadir el nuevo caracter al texto cifrado
      texto_cifrado += nuevo_caracter
    # Si el caracter es una letra minúscula
    elif caracter in string.ascii_lowercase:
      # Repetir los mismos pasos que para las mayúsculas pero usando "a" en lugar de "A"
      numero = ord(caracter) - ord("a")
      nuevo_numero = (numero + desplazamiento) % 26
      nuevo_caracter = chr(nuevo_numero + ord("a"))
      texto_cifrado += nuevo_caracter
    # Si el caracter no es una letra, lo dejamos igual
    else:
      texto_cifrado += caracter
  
  # Devolver el texto cifrado
  return texto_cifrado

# Función para descifrar un texto con el cifrado César
def descifrar(texto, desplazamiento):
  # Inicializar el texto descifrado vacío
  texto_descifrado = ""
  # Recorrer cada caracter del texto
  for caracter in texto:
    # Si el caracter es una letra mayúscula
    if caracter in string.ascii_uppercase:
      # Obtener el número correspondiente al caracter (de 0 a 25)
      numero = ord(caracter) - ord("A")
      # Restar el desplazamiento y aplicar el módulo 26 para obtener el nuevo número
      nuevo_numero = (numero - desplazamiento) % 26 
      # Obtener el nuevo caracter correspondiente al nuevo número 
      nuevo_caracter = chr(nuevo_numero + ord("A"))
       # Añadir el nuevo caracter al texto descifrado 
       text_descifradotexto_descifradotexto_descifradoxto_descifradoxto_descifradoxto_descifradoxto_descifradoxto_descifradoxto_descifradoxto_descifradoxto_descifradoxto_descifradoxto_ += nuevocaracternuevo_caracternuevo_caracternuevo_caracternuevo_caracternuevo_caracternuevo_caracternuevo_caracternuevo_caracternuevocaracternuevocaracternuevocaracternuevocaractercara_
    elif character in string.ascii_lowercase: 
     number=ord(character)-ord('a') 
     new_number=(number-desplazamientodesplazamientodesplazamientodesplazamientodesplazamientodespla_)%26 
     new_character=chr(new_number+ord('a')) 
     text_decrypted+=new_character 
   else: 
     text_decrypted+=character 
  
 return text_decrypted 

# Ejemplo de uso de las funciones

texto_original="Hola mundo"
desplazamiento=3

texto_cifrado=cifar(texto_original,desplazamiento)
print(texto_cifrado)

texto_descrifado=descifar(texto_cifradotexto_cifradotexto_cifradotexto_,despla_)
print(texto_descriado)