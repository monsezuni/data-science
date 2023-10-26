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

def promedio(n):
    '''Funcion que retorna el promedio de una lista de numeros
    
    Entrada
    -------
    n : numeros a utilizar
    
    Salida
    ------
    promedio : suma de todos los numeros dividida en su cantidad
    ''' 
    if len(n) == 0:
        return 0
    suma = sum(n)
    prom = suma / len(n)
    return prom

def mediana(n):
    '''Funcion que retorna la mediana de una lista de numeros
    
    Entrada
    -------
    n : ordena la lista
    
    Salida
    ------
    mediana : identifica si la cantidad de numeros es par o impar y retorna su mediana
    '''
    
    n.sort()
    m = len(n)
    
    if m % 2 != 0:
        median = n[(m + 1) // 2]
    else:
        median = (n[(m // 2) - 1] + n[m // 2]) / 2

    return median

def rango(n):
    '''Funcion que retorna el rango de un listado de numeros
    
    Entrada
    -------
    numeros: realiza el rango mediante la lista
    
    Salida
    ------
    rango: retorna el rango mediante una resta
    '''
    rango = max(n)-min(n)
    
    return rango

def varianza(n):
    '''Funcion que retorna la varianza de un listado de numeros
    
    Entrada
    -------
    num: listado de numeros
    
    Salida
    ------
    varianza: division de la suma de los cuadrados de las diferencias por el numero de datos
    '''
    media = sum(n)/len(n)
    suma = sum((x - media)**2 for x in n)
    var = suma/len(n)
    return var

def cuartiles(n):
    '''Funcion que retorna los cuartiles de datos ordenados
    
    Entrada
    -------
    n: ordenar la lista de datos y calcular los cuartiles
    
    Salida
    ------
    cuartil: retorna los calculos realizados para los cuartiles
    '''
    datos2 = sorted(n)
    b = len(datos2)
    if b % 4 == 0:
        medio = b // 2
        Q1 = (datos2[:medio])[len(datos2[:medio]) // 2]
        Q3 = (datos2[medio:])[len(datos2[medio:]) // 2]
    else:
        medio = b // 2
        Q1 = datos2[:medio][len(datos2[:medio]) // 2]
        Q3 = datos2[medio+1:][len(datos2[medio+1:]) // 2]

    Q2 = mediana(datos2)
    return Q1, Q2, Q3

def rango_intercuartil(n):
    '''Funcion que retorna el rango intercuartil de una lista de datos
    
    Entrada
    -------
    n: datos ordenados
    
    Salida
    ------
    iqr: al calcular el cuartil 1 y 3 retorna el rango intercuartil
    '''
    q1, q2, q3 = cuartiles(n)

    IQR = q3 - q1
    return IQR

def desv_estandar(n):
    '''Funcion que retorna la desviacion estandar de un listado de numeros
    
    Entrada
    ------- 
    n: se determina la varianza para calcular su desviacion
    
    Salida
    ------
    desv: se saca la raiz cuadrada de la varianza
    '''
    n.sort()
    m = len(n)
    
    if m % 2 != 0:
        median = n[(m + 1) // 2]
    else:
        median = (n[(m // 2) - 1] + n[m // 2]) / 2

    suma = sum((x - median)**2 for x in n)
    
    varianza = suma/len(n)
    
    desviacion_estandar = varianza ** 0.5
    
    return desviacion_estandar

def MAD(n):
    '''Funcion que retorna MAD de los datos
    
    Entrada
    -------
    n: datos ordenados, se calcula su mediana
    
    Salida
    ------
    mad: se calculan las diferencias absolutas de cada dato y la mediana de aquellas para retornar en mad
    '''
    median = mediana(n)
    desv_absoluta = [abs(n - median) for x in n]
    mda = mediana(desv_absoluta)
    return mda
