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
En el punto 1 del plantemamiento de la prueba se solicita descargar el contenido desde la URL:
https://rapidapi.com/apilayernet/api/rest-countries-v1

Esta URL responde con un JSON, aunque necesita un **TOKENID** para poder hacerlo. Para tal fin se debe crear una cuenta, obtener el **TOKENID** y con la URL https://restcountries-v1.p.rapidapi.com/all se debe pasar por parámetro en una petición GET lo siguiente: **rapidapi-key=TOKENID** de la siguiente forma:
https://restcountries-v1.p.rapidapi.com/all?rapidapi-key=XXXXXXXXXXXXXX
Luego de recibir la repuesta se debe convertir en un tipo **json** para poder usar sus datos de manera conveniete.

Para realizar dicha acción se necesita el módulo
**requests**. Este módulo se puede instalar en python por medio del siguiente comando:
**pip install requests**

**Sin embargo**, en la solución se implementarán funciones de instalación automática para tales fines.








