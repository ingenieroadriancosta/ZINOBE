**Tabla de contenido**
- [1 - PLANTEAMIENTO DE LA PRUEBA](#1---planteamiento-de-la-prueba)
- [2 - PLANTEAMIENTO DE LA SOLUCION](#2---planteamiento-de-la-solucion)
- [3 - EJECUCION DE LA SOLUCION](#3---ejecucion-de-la-solucion)
- [4 - PRUEBAS UNITARIAS](#4---pruebas-unitarias)
- [5 - MONTAJE DEL SERVIDOR](#5---montaje-del-servidor)
- [6 - ACERCA DEL ARCHIVO HTML INDEX](#6---acerca-del-archivo-html-index)
- [7 - BASE DE DATOS](#7---base-de-datos)



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



# 2 - PLANTEAMIENTO DE LA SOLUCION
1. En el punto 1 del plantemamiento de la prueba se solicita descargar el contenido desde la URL: https://rapidapi.com/apilayernet/api/rest-countries-v1 . Esta URL responde con un JSON, aunque necesita un **TOKENID** para poder hacerlo. Para tal fin se debe crear una cuenta, obtener el **TOKENID** y con la URL https://restcountries-v1.p.rapidapi.com/all se debe pasar por parámetro en una petición GET lo siguiente: **rapidapi-key=TOKENID** de la siguiente forma:
https://restcountries-v1.p.rapidapi.com/all?rapidapi-key=XXXXXXXXXXXXXX
Para realizar dicha acción se necesita el módulo **requests**. Este módulo se puede instalar en *python* por medio del siguiente comando: **`pip install requests`**, **Sin embargo**, en la solución se implementarán funciones de instalación automática para tales fines.
Una vez se obtienen los datos de la URL se convierten a **JSON** por medio del módulo **json** que está en *python*.
2. Para el punto 2 del **plantemamiento de la prueba** se realizan las mismas acciones de descarga y conversión que en el punto 1.
3. Para el punto tres se utiliza el módulo **`hashlib`** en *python*, este permite la encripción en `SHA1`.
4. Para la medición del tiempo se usa el módulo **`time`** en *python*. Pro medio de este y sus funciones se mide el tiempo en el que comienza la busqueda y el armado de la fila.
5. Una vez se tengan los datos organizados en un diccionario de *python* se utiliza el módulo pandas para crear el `DataFrame`. El módulo es externo a *python* y debe ser instalado por medio del comando:
**`pip install pandas`**
sin embargo tambien se realizará de manera automática.
6. Para obtener los datos como *tiempo total, tiempo promedio, tiempo minimo y tiempo maximo* de procesamiento para cada fila se usarán las funciones de `DataFrame` **sum, mean, min y max**.
7. Para guardar los datos en sqlite3 se usa el módulo `sqlite3` de *python*.
8. Para generar el archivo **JSON** se usará la función **to_json** de `DataFrame`.




# 3 - EJECUCION DE LA SOLUCION

Todo el código está en la carpeta **src**. En ella se encuentran tres archivos fundamentales como son:

- **index.py**
- **manyfuncs.py**
- **index.html**

Debe ejecutarse el siguiente comando:
**`python index.py`**



# 4 - PRUEBAS UNITARIAS

Para las pruebas unitarias se probará la función **`procs`** que es la que se encarga de realizar todos los requerimientos y usa todas las funciones en `index.py` y `manyfuncs.py`.

El módulo que se encarga de realizar las pruebas unitarias es **`TestZINOBE.py`**. Para realizar la prueba se ejecuta el siguiente comando:
**`python TestZINOBE.py`**
El contenido es el siguiente:
```python
import unittest
import index 
class TestMyModule(unittest.TestCase):
    def test_index_procs(self):
        print("RESULTADO DE LA PRUEBA: FUNCION index.procs()")
        self.assertIsNotNone(index.procs())

if __name__ == "__main__":
    print("-----------------------------------------")
    print("PRUEBAS UNITARIAS DEL PROYECTO ZINOBE")
    print("-----------------------------------------\n\n")
    unittest.main()
```
Despues de realizar la prueba no hubo ninguna advertencia ni error.


# 5 - MONTAJE DEL SERVIDOR
El servidor se ha montado con el módulo **`http.server`** de python.
Un servidor básico se ha desarrollado y se describe con el siguiente código:
```python
class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            htmlcontent = procs()
            self.wfile.write( htmlcontent.encode('utf8') )
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)
def main():
    try:
        port = 8000
        server = HTTPServer(('', port), WebServerHandler)
        webbrowser.open_new( "http://localhost:%s/" % port )
        server.serve_forever()
    except KeyboardInterrupt:
        print (" ^C entered, stopping web server....")
        server.socket.close()
        print("FIN")

if __name__ == '__main__':
    main()
```
Para este caso, el servidor estará en:
**http://localhost:8000**
La función **`procs()`** devuelve el contenido ya organizado para el cliente.



# 6 - ACERCA DEL ARCHIVO HTML INDEX
En el archivo **`index.html`** se almacena la estructura básica de una pagina HTML, pero además se utiliza para rellenar las tablas.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>
    <h2>PRUEBA TECNICA ZINOBE</h2>
    <h5>Desarrollada por <b><em>Adrián Costa</em></b></h5>
    <p>La base de datos se encuentra como (<b>ZINOBE.db</b>)</p>
    <table class='table table-bordered table-responsive-sm' 
                style='width:80%; text-align: center; vertical-align: middle;' >
{% tabla de contenido %}
    </table>
    <br>
    <h3><b>TABLA DE TIEMPOS(ms)</b></h3>
    <table class='table table-bordered table-responsive-sm' 
                style='width:80%; text-align: center; vertical-align: middle;' >
        <tr>
            <th scope='col'>TOTAL</th>
            <th scope='col'>PROMEDIO</th>
            <th scope='col'>MÍNIMO</th>
            <th scope='col'>MÁXIMO</th>
        </tr>
{% tabla de tiempos %}
    </table>
</body>
</html>
```
En el campo **{% tabla de contenido %}** se cambia dicho contenido por una estructura adecuada para la tabla:

|  Region | City Name |  Languaje | Time  |
|---|---|---|---|
|  **...** | **...**  |  **...** | **...**  |
| **...**  | **...**  | **...**  | **...**  |
| **...**  | **...**  | **...**  | **...**  |
<br>
<br>

En el campo **{% tabla de tiempos %}** se cambia por un contenido en el cual se presentan los tiempos total, mínimo, máximo etc.

# 7 - BASE DE DATOS


<br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br>


