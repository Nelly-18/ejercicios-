#EJERCICIO 1
def contar_ocurrencias(palabras):
    ocurrencias = {}
    for palabra in palabras:
        ocurrencias[palabra] = ocurrencias.get(palabra, 0) + 1
    return ocurrencias

palabras = ["python", "java", "python", "c++"]
print(contar_ocurrencias(palabras))

#EJERCICIO 2
def combinar_diccionarios(dic1, dic2):
    resultado = dic1.copy()
    for clave, valor in dic2.items():
        resultado[clave] = resultado.get(clave, 0) + valor
    return resultado

dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}
print(combinar_diccionarios(dic1, dic2))

#EJERCICIO 3
def frecuencia_numeros(numeros):
    frecuencia = {}
    for num in numeros:
        frecuencia[num] = frecuencia.get(num, 0) + 1
    return frecuencia

numeros = [1, 1, 2, 3, 3, 3]
print(frecuencia_numeros(numeros))

#EJERCICIO 4
def filtrar_palabras_largas(palabras, longitud):
    return [palabra for palabra in palabras if len(palabra) > longitud]

palabras = ["hola", "mundo", "python", "programación"]
longitud = 5
print(filtrar_palabras_largas(palabras, longitud)) 


#EJERCICIO 5
def invertir_tuplas(tuplas):
    return [(b, a) for a, b in tuplas]

tuplas = [(1, 2), (3, 4), (5, 6)]
print(invertir_tuplas(tuplas)) 

#EJERCICIO 6
def valor_mas_frecuente(numeros):
    
    frecuencias = {}

    for num in numeros:
        if num in frecuencias:
            frecuencias[num] += 1
        else:
            frecuencias[num] = 1

    max_frecuencia = 0
    valor_max_frecuencia = None
    
    for num, freq in frecuencias.items():
        if freq > max_frecuencia:
            max_frecuencia = freq
            valor_max_frecuencia = num
    return valor_max_frecuencia

#EJERCICIO 7
def es_subconjunto(conjunto1, conjunto2):
    return conjunto1.issubset(conjunto2)

conjunto1 = {1, 2, 3}
conjunto2 = {1, 2, 3, 4, 5}
print(es_subconjunto(conjunto1, conjunto2)) 

#EJERCICIO 8
def agrupar_por_edad(personas):
    grupos = {}
    for persona in personas:
        edad = persona['edad']
        if edad not in grupos:
            grupos[edad] = []
        grupos[edad].append(persona['nombre'])
    return grupos

personas = [{"nombre": "Ana", "edad": 25}, {"nombre": "Luis", "edad": 25}, {"nombre": "Carlos", "edad": 30}]
print(agrupar_por_edad(personas)) 

#EJERCICIO 9
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

numeros = [5, 3, 8, 6, 2]
print(merge_sort(numeros)) 

#EJERCICIO 10
def eliminar_menores(numeros, limite):
    return [num for num in numeros if num >= limite]

numeros = [1, 2, 3, 4, 5]
limite = 3
print(eliminar_menores(numeros, limite))  

#EJERCICIO 11
def aplanar_lista(lista_de_listas):
    return [elemento for sublista in lista_de_listas for elemento in sublista]

lista_de_listas = [[1, 2], [3, 4], [5]]
print(aplanar_lista(lista_de_listas)) 

#EJERCICIO 12
def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    if n % 2 == 1:
        return numeros_ordenados[n // 2]
    else:
        medio = n // 2
        return (numeros_ordenados[medio - 1] + numeros_ordenados[medio]) / 2

numeros = [1, 3, 2, 4, 5]
print(calcular_mediana(numeros))  

#EJERCICIO 13
def duplicar_elementos(numeros):
    return [num for num in numeros for _ in range(2)]

numeros = [1, 2, 3]
print(duplicar_elementos(numeros))

#EJERCICIO 14
def contar_palabras(frases):
    return {i: len(frase.split()) for i, frase in enumerate(frases)}

frases = ["Hola mundo", "Python es genial", "Me gusta programar"]
print(contar_palabras(frases))

#EJERCICIO 15
def clave_maxima(diccionario):
    return max(diccionario, key=diccionario.get)

diccionario = {'a': 10, 'b': 20, 'c': 5}
print(clave_maxima(diccionario)) 

#EJERCICIO 16
def encontrar_palindromos(palabras):
    return [palabra for palabra in palabras if palabra == palabra[::-1]]

palabras = ["ana", "oso", "hola", "level"]
print(encontrar_palindromos(palabras))




























