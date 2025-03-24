# 1. Declarar una lista vacía
lista_vacia = []

# 2. Declarar una lista con más de 5 elementos
mi_lista = [1, 2, 3, 4, 5, 6, 7]

# 3. Encontrar la longitud de la lista
longitud_lista = len(mi_lista)
print("Longitud de la lista:", longitud_lista)

# 4. Obtener el primer elemento, el elemento del medio y el último elemento de la lista
primer_elemento = mi_lista[0]
elemento_medio = mi_lista[len(mi_lista) // 2]
ultimo_elemento = mi_lista[-1]
print("Primer elemento:", primer_elemento, "Elemento del medio:", elemento_medio, "Último elemento:", ultimo_elemento)

# 5. Declarar una lista llamada tipos_de_datos_mixtos
tipos_de_datos_mixtos = ["Juan", 30, 1.75, "Soltero", "Calle Falsa 123"]

# 6. Declarar una lista llamada empresas_it con valores iniciales
empresas_it = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Imprimir la lista usando print()
print("Empresas de IT:", empresas_it)

# 8. Imprimir el número de empresas en la lista
print("Número de empresas:", len(empresas_it))

# 9. Imprimir la primera, la del medio y la última empresa
print("Primera empresa:", empresas_it[0])
print("Empresa del medio:", empresas_it[len(empresas_it) // 2])
print("Última empresa:", empresas_it[-1])

# 10. Imprimir la lista después de modificar una de las empresas
empresas_it[1] = "Alphabet"
print("Empresas de IT modificadas:", empresas_it)

# 11. Agregar una empresa de IT a la lista
empresas_it.append("Tesla")
print("Empresas de IT después de agregar:", empresas_it)

# 12. Insertar una empresa de IT en el medio de la lista
empresas_it.insert(len(empresas_it) // 2, "Netflix")
print("Empresas de IT después de insertar:", empresas_it)

# 13. Cambiar el nombre de una empresa a mayúsculas (excepto IBM)
empresas_it[3] = empresas_it[3].upper()
print("Empresas de IT después de cambiar a mayúsculas:", empresas_it)

# 14. Unir las empresas de IT con una cadena '#;  '
empresas_unidas = '#;  '.join(empresas_it)
print("Empresas unidas:", empresas_unidas)

# 15. Verificar si una empresa específica existe en la lista
empresa_a_verificar = "Google"
print(f"¿{empresa_a_verificar} está en la lista? {empresa_a_verificar in empresas_it}")

# 16. Ordenar la lista usando el método sort()
empresas_it.sort()
print("Empresas de IT ordenadas:", empresas_it)

# 17. Invertir la lista en orden descendente usando reverse()
empresas_it.reverse()
print("Empresas de IT en orden descendente:", empresas_it)

# 18. Obtener las primeras 3 empresas de la lista
primeras_tres = empresas_it[:3]
print("Primeras tres empresas:", primeras_tres)

# 19. Obtener las últimas 3 empresas de la lista
ultimas_tres = empresas_it[-3:]
print("Últimas tres empresas:", ultimas_tres)

# 20. Obtener la empresa del medio o las empresas del medio
indice_medio = len(empresas_it) // 2
empresa_medio = empresas_it[indice_medio] if len(empresas_it) % 2 != 0 else empresas_it[indice_medio-1:indice_medio+1]
print("Empresa(s) del medio:", empresa_medio)

# 21. Eliminar la primera empresa de IT de la lista
empresas_it.pop(0)
print("Empresas de IT después de eliminar la primera:", empresas_it)

# 22. Eliminar la empresa del medio o las empresas del medio
indice_medio = len(empresas_it) // 2
if len(empresas_it) % 2 != 0:
    empresas_it.pop(indice_medio)
else:
    empresas_it.pop(indice_medio - 1)
    empresas_it.pop(indice_medio - 1)
print("Empresas de IT después de eliminar la(s) del medio:", empresas_it)

# 23. Eliminar la última empresa de IT de la lista
empresas_it.pop(-1)
print("Empresas de IT después de eliminar la última:", empresas_it)

# 24. Eliminar todas las empresas de IT de la lista
empresas_it.clear()
print("Empresas de IT después de eliminar todas:", empresas_it)

# 25. Destruir la lista de empresas de IT
del empresas_it
# print(empresas_it)  # Esto dará un error porque la lista ya no existe

# 26. Unir las siguientes listas:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end

# 27. Insertar Python y SQL después de Redux en la lista full_stack
full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Python") + 1, "SQL")
print("Full Stack después de insertar Python y SQL:", full_stack)


#exercice 2

# Lista de edades de 10 estudiantes
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Ordenar la lista y encontrar la edad mínima y máxima
edades.sort()
edad_minima = min(edades)
edad_maxima = max(edades)
print("Edades ordenadas:", edades)
print("Edad mínima:", edad_minima)
print("Edad máxima:", edad_maxima)

# 2. Agregar la edad mínima y máxima nuevamente a la lista
edades.append(edad_minima)
edades.append(edad_maxima)
print("Edades después de agregar mínima y máxima:", edades)

# 3. Encontrar la mediana de las edades
longitud_edades = len(edades)
if longitud_edades % 2 == 0:
    mediana = (edades[longitud_edades // 2 - 1] + edades[longitud_edades // 2]) / 2
else:
    mediana = edades[longitud_edades // 2]
print("Mediana de las edades:", mediana)

# 4. Encontrar la edad promedio
promedio_edades = sum(edades) / len(edades)
print("Edad promedio:", promedio_edades)

# 5. Encontrar el rango de las edades (máximo - mínimo)
rango_edades = edad_maxima - edad_minima
print("Rango de las edades:", rango_edades)

# 6. Comparar los valores de (mínimo - promedio) y (máximo - promedio) usando abs()
diferencia_min = abs(edad_minima - promedio_edades)
diferencia_max = abs(edad_maxima - promedio_edades)
print("Diferencia entre mínima y promedio:", diferencia_min)
print("Diferencia entre máxima y promedio:", diferencia_max)

# 7. Encontrar el/los país(es) del medio en la lista de países
paises = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
longitud_paises = len(paises)
if longitud_paises % 2 == 0:
    paises_medios = paises[longitud_paises // 2 - 1:longitud_paises // 2 + 1]
else:
    paises_medios = [paises[longitud_paises // 2]]
print("País(es) del medio:", paises_medios)

# 8. Dividir la lista de países en dos listas iguales (o una más grande si es impar)
mitad = (longitud_paises + 1) // 2  # Asegura que la primera mitad sea más grande si es impar
primera_mitad = paises[:mitad]
segunda_mitad = paises[mitad:]
print("Primera mitad de países:", primera_mitad)
print("Segunda mitad de países:", segunda_mitad)

# 9. Desempaquetar los primeros tres países y el resto como países escandinavos
primeros_tres, *paises_escandinavos = paises
print("Primeros tres países:", primeros_tres)
print("Países escandinavos:", paises_escandinavos)