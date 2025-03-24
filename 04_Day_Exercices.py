# 1. Concatenar cadenas
cadena1 = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
cadena2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(cadena1)  # Salida: 'Thirty Days Of Python'
print(cadena2)  # Salida: 'Coding For All'

# 2. Declarar una variable y asignarle un valor
empresa = "Coding For All"
print(empresa)  # Salida: 'Coding For All'

# 3. Imprimir la longitud de la cadena
print(len(empresa))  # Salida: 15

# 4. Cambiar todos los caracteres a mayúsculas
print(empresa.upper())  # Salida: 'CODING FOR ALL'

# 5. Cambiar todos los caracteres a minúsculas
print(empresa.lower())  # Salida: 'coding for all'

# 6. Usar los métodos capitalize(), title(), swapcase()
print(empresa.capitalize())  # Salida: 'Coding for all'
print(empresa.title())  # Salida: 'Coding For All'
print(empresa.swapcase())  # Salida: 'cODING fOR aLL'

# 7. Cortar la primera palabra
print(empresa.split(' ', 1)[1])  # Salida: 'For All'

# 8. Comprobar si la cadena contiene la palabra 'Coding'
print('Coding' in empresa)  # Salida: True

# 9. Reemplazar la palabra 'Coding' por 'Python'
print(empresa.replace('Coding', 'Python'))  # Salida: 'Python For All'

# 10. Reemplazar 'Python for Everyone' por 'Python for All'
oracion = 'Python for Everyone'
print(oracion.replace('Everyone', 'All'))  # Salida: 'Python for All'

# 11. Dividir la cadena 'Coding For All' por espacio
print(empresa.split())  # Salida: ['Coding', 'For', 'All']

# 12. Dividir la cadena con comas
empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(empresas.split(', '))  # Salida: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 13. Encontrar el carácter en el índice 0 de 'Coding For All'
print(empresa[0])  # Salida: 'C'

# 14. Encontrar el último índice de 'Coding For All'
print(len(empresa) - 1)  # Salida: 14

# 15. Carácter en el índice 10 de 'Coding For All'
print(empresa[10])  # Salida: 'A'

# 16. Crear un acrónimo para 'Python For Everyone'
acronimo1 = ''.join([palabra[0] for palabra in 'Python For Everyone'.split()])
print(acronimo1)  # Salida: 'PFE'

# 17. Crear un acrónimo para 'Coding For All'
acronimo2 = ''.join([palabra[0] for palabra in 'Coding For All'.split()])
print(acronimo2)  # Salida: 'CFA'

# 18. Usar index para encontrar la posición de la primera aparición de 'C' en 'Coding For All'
print(empresa.index('C'))  # Salida: 0

# 19. Usar index para encontrar la posición de 'F' en 'Coding For All'
print(empresa.index('F'))  # Salida: 7

# 20. Usar rfind para encontrar la última aparición de 'l' en 'Coding For All People'
print(empresa.rfind('l'))  # Salida: 14

# 21. Usar index o find para encontrar la primera aparición de 'because' en la oración
oracion = 'You cannot end a sentence with because because because is a conjunction'
print(oracion.find('because'))  # Salida: 34

# 22. Usar rindex para encontrar la última aparición de 'because'
print(oracion.rindex('because'))  # Salida: 57

# 23. Cortar la frase 'because because because' de la oración
print(oracion[34:57])  # Salida: 'because because because'

# 24. ¿'Coding For All' empieza con 'Coding'?
print(empresa.startswith('Coding'))  # Salida: True

# 25. ¿'Coding For All' termina con 'coding'?
print(empresa.endswith('coding'))  # Salida: False

# 26. Eliminar los espacios de izquierda y derecha de '   Coding For All      '
print('   Coding For All      '.strip())  # Salida: 'Coding For All'

# 27. ¿Cuál de estas variables es un identificador?
# '30DaysOfPython' es válido porque comienza con un número
# 'thirty_days_of_python' es válido porque sigue las reglas de nombres de variables en Python.
print('30DaysOfPython'.isidentifier())  # Salida: True
print('thirty_days_of_python'.isidentifier())  # Salida: True

# 28. Unir la lista con un hash y espacio
bibliotecas_python = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(bibliotecas_python))  # Salida: 'Django # Flask # Bottle # Pyramid # Falcon'

# 29. Usar la secuencia de escape de nueva línea
print("I am enjoying this challenge.\nI just wonder what is next.")

# 30. Usar la secuencia de escape de tabulación
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# 31. Formateo de cadenas para mostrar el área de un círculo
radio = 10
area = 3.14 * radio ** 2
print(f"The area of a circle with radius {radio} is {area} meters square.")  # Salida: 'The area of a circle with radius 10 is 314 meters square.'

# 32. Formateo de cadenas para operaciones aritméticas
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")