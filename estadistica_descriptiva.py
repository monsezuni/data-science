#!/usr/bin/env python
# coding: utf-8

# In[1]:


def moda(n):
    '''Función que retorna la moda de una cantidad de datos.
    
    Entrada
    -------
    n : lista de datos.
    
    Salida
    ------
    moda : str
    '''
    categorias = []
    for i in n:
        if i not in categorias:
            categorias.append(i)
    cuentas = []
    for c in categorias:
        x = 0
        for val in n:
            if val == c:
                x = x + 1
        cuentas.append(x)
        
    i_max = 0  
    val_max = cuentas[0]
    for m in range(1, len(cuentas)):
        if cuentas[m] > val_max:
            i_max = m
            val_max = cuentas[m]
            
    moda = categorias[i_max]
    return moda

            
    


# In[1]:


def promedio(numeros):
    '''Funcion que retorna el promedio de una lista de numeros
    
    Entrada
    -------
    numeros : numeros a utilizar
    
    Salida
    ------
    promedio : suma de todos los numeros dividida en su cantidad
    ''' 
    if len(numeros) == 0:
        return 0
    suma = sum(numeros)
    prom = suma / len(numeros)
    return prom


# In[2]:


def mediana(numero):
    '''Funcion que retorna la mediana de una lista de numeros
    
    Entrada
    -------
    numero : ordena la lista
    
    Salida
    ------
    mediana : identifica si la cantidad de numeros es par o impar y retorna su mediana
    '''
    
    lista = sorted(numero)
    m = len(lista)
    
    if m % 2 == 1:
        median = lista[m // 2]
    else:
        median = (lista[(m // 2) - 1] + lista[m // 2]) / 2

    return median


# In[3]:


def rango(numeros):
    '''Funcion que retorna el rango de un listado de numeros
    
    Entrada
    -------
    numeros: realiza el rango mediante la lista
    
    Salida
    ------
    rango: retorna el rango mediante una resta
    '''
    rango = max(numeros)-min(numeros)
    
    return rango


# In[9]:


def varianza(num):
    '''Funcion que retorna la varianza de un listado de numeros
    
    Entrada
    -------
    num: listado de numeros
    
    Salida
    ------
    varianza: division de la suma de los cuadrados de las diferencias por el numero de datos
    '''
   
    lista = sorted(num)
    m = len(lista)
    
    if m % 2 == 1:
        median = lista[m // 2]
    else:
        median = (lista[(m // 2) - 1] + lista[m // 2]) / 2

    suma = sum((x - median)**2 for x in num)
    
    varianza = suma/len(num)
    
    return varianza


# In[5]:


def cuartiles(datos):
    '''Funcion que retorna los cuartiles de datos ordenados
    
    Entrada
    -------
    datos: ordenar la lista de datos y calcular los cuartiles
    
    Salida
    ------
    cuartil: retorna los calculos realizados para los cuartiles
    '''
    datos2 = sorted(datos)
    b = len(datos2)

    if b % 4 == 0:
        Q1 = (datos2[b // 4 - 1] + datos2[b // 4]) / 2
    else:
        Q1 = datos2[b // 4]

    if b % 2 == 0:
        Q2 = (datos2[b // 2 - 1] + datos2[b // 2]) / 2
    else:
        Q2 = datos2[b // 2]
        
    if b % 4 == 0:
        Q3 = (datos2[3 * b // 4 - 1] + datos2[3 * b // 4]) / 2
    else:
        Q3 = datos2[3 * b // 4]

    return Q1, Q2, Q3


# In[12]:


def rango_intercuartil(dato):
    '''Funcion que retorna el rango intercuartil de una lista de datos
    
    Entrada
    -------
    dato: datos ordenados
    
    Salida
    ------
    iqr: al calcular el cuartil 1 y 3 retorna el rango intercuartil
    '''
    rangoint = sorted(dato)
    a = len(rangoint)

    # Calcula el primer cuartil (Q1)
    if a % 4 == 0:
        q1 = (rangoint[a // 4 - 1] + rangoint[a // 4]) / 2
    else:
        q1 = rangoint[a // 4]

    # Calcula el tercer cuartil (Q3)
    if a % 4 == 0:
        q3 = (rangoint[3 * a // 4 - 1] + rangoint[3 * a // 4]) / 2
    else:
        q3 = rangoint[3 * a // 4]

    IQR = q3 - q1
    return IQR


# In[10]:


def desv_estandar(num):
    '''Funcion que retorna la desviacion estandar de un listado de numeros
    
    Entrada
    ------- 
    num: se determina la varianza para calcular su desviacion
    
    Salida
    ------
    desv: se saca la raiz cuadrada de la varianza
    '''
    lista = sorted(num)
    m = len(lista)
    
    if m % 2 == 1:
        median = lista[m // 2]
    else:
        median = (lista[(m // 2) - 1] + lista[m // 2]) / 2

    suma = sum((x - median)**2 for x in num)
    
    varianza = suma/len(num)
    
    desviacion_estandar = varianza ** 0.5
    
    return desviacion_estandar


# In[11]:


def MAD(datos):
    '''Funcion que retorna MAD de los datos
    
    Entrada
    -------
    datos: datos ordenados, se calcula su mediana
    
    Salida
    ------
    mad: se calculan las diferencias absolutas de cada dato y la mediana de aquellas para retornar en mad
    '''
    n = len(datos)

    dato_ordenado = sorted(datos)
    if n % 2 == 0:
        mediana = (dato_ordenado[n // 2 - 1] + dato_ordenado[n // 2]) / 2
    else:
        mediana = dato_ordenado[n // 2]

    dif_absolutas = [abs(x - mediana) for x in datos]

    dif_absolutas_ordenadas = sorted(dif_absolutas)
    if n % 2 == 0:
        mad = (dif_absolutas_ordenadas[n // 2 - 1] + dif_absolutas_ordenadas[n // 2]) / 2
    else:
        mad = dif_absolutas_ordenadas[n // 2]

    return mad


# In[ ]:




