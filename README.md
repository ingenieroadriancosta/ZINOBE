**Tabla de contenido**
[TOC]
<br>
<br>
<br>
# 1 - PLANTEAMIENTO DE LA PRUEBA
|  Region | City Name |  Languaje | Time  |
|---|---|---|---|
|  Africa | Angola  |  AF4F4762F9BD3F0F4A10CAF5B6E63DC4CE543724 | 0.23 ms  |
|   |   |   |   |
|   |   |   |   |

Desarrolle una aplicacion en python que genere la tabla anterior teniendo las siguientes consideraciones:

1. De https://rapidapi.com/apilayernet/api/rest-countries-v1, obtenga todas las regiones existentes.
2. De https://restcountries.eu/ Obtenga un pais por region apartir de la region optenida del punto 1.
3. De https://restcountries.eu/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1
4. En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico)
5. La tabla debe ser creada en un DataFrame con la libreria PANDAS
6. Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
7. Guarde el resultado en sqlite.
8. Genere un Json de la tabla creada y guardelo como data.json
9. La prueba debe ser entregada en un repositorio git.


**Es un plus si:**
* No usa famework
* Entrega Test Unitarios
* Presenta un diseño de su solucion.



# 2 - DISEÑO DE LA SOLUCION
1. En el punto 1 del plantemamiento de la prueba se solicita descargar el contenido desde la URL:
<br>
https://rapidapi.com/apilayernet/api/rest-countries-v1
<br>
Esta URL responde con un JSON, aunque necesita un **TOKENID** para poder hacerlo. Para tal fin se debe crear una cuenta, obtener el **TOKENID** y con la URL https://restcountries-v1.p.rapidapi.com/all se debe pasar por parámetro en una petición GET lo siguiente: **rapidapi-key=TOKENID** de la siguiente forma:
https://restcountries-v1.p.rapidapi.com/all?rapidapi-key=XXXXXXXXXXXXXX
Para realizar dicha acción se necesita el módulo **requests**. Este módulo se puede instalar en *python* por medio del siguiente comando:
<br>
**`pip install requests`**
<br>
**Sin embargo**, en la solución se implementarán funciones de instalación automática para tales fines.
Una vez se obtienen los datos de la URL se convierten a **JSON** por medio del módulo **json** que está en *python*.
<br>
<br>
2. Para el punto 2 del **plantemamiento de la prueba** se realizan las mismas acciones de descarga y conversión que en el punto 1.
<br>
3. Para el punto tres se utiliza el módulo **`hashlib`** en *python*, este permite la encripción en `SHA1`.
<br>
4. Para la medición del tiempo se usa el módulo **`time`** en *python*. Pro medio de este y sus funciones se mide el tiempo en el que comienza la busqueda y el armado de la fila.
<br>
5. Una vez se tengan los datos organizados en un diccionario de *python* se utiliza el módulo pandas para crear el `DataFrame`. El módulo es externo a *python* y debe ser instalado por medio del comando:
**`pip install pandas`**
sin embargo tambien se realizará de manera automática.
<br>
6. Para obtener los datos como *tiempo total, tiempo promedio, tiempo minimo y tiempo maximo* de procesamiento para cada fila se usarán las funciones de `DataFrame` **sum, mean, min y max**.
<br>
7. Para guardar los datos en sqlite3 se usa el módulo `sqlite3` de *python*.
<br>
8. Para generar el archivo **JSON** se usará la función **to_json** de `DataFrame`.


<br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br>

