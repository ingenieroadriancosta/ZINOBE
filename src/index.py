import manyfuncs  as mf
mf.getimports()
###############################################################################
from http.server import BaseHTTPRequestHandler, HTTPServer
import io, os, webbrowser, time, json, sys
import pandas as pds
###############################################################################
###############################################################################
## LA FUNCIÓN (procs()) 
## REALIZA TODA LA PETICIÓN DE LA PRUEBA Y LO DEVUELVE AL
## CLIENTE
def procs():
    try:
        ###############################################################################
        ## URLs de las APIs necesarias.
        url1 = 'https://restcountries-v1.p.rapidapi.com/all?rapidapi-key=' + mf.get_ulr_response_as_txt('http://adriancosta.000webhostapp.com/files/tkid.txt')
        url2 = 'https://restcountries.eu/rest/v2/all'
        # DESCARGAR DE "URL1"
        x = mf.get_ulr_response_as_json(url1)
        # DESCARGAR DE "URL2"
        y = mf.get_ulr_response_as_json(url2)
        ##
        allregions = []
        table = []
        ti = time.perf_counter()
        #
        ## obtener regiones
        for t in reversed( range(len(y)) ):
            ss = x[t]['region']
            matching = [s for s in allregions if ss in s]
            if not matching:
                allregions.append(ss)
                te = time.perf_counter()
                tc = 1000*(te - ti) 
                dtmp = { 'Region':y[t]['region'], 'City Name': y[t]['name'], 'Languaje': mf.tosha1(y[t]['languages'][0]['name']),'Time':tc}
                table.append( dtmp )
                ti = time.perf_counter()
        #
        # CREAR DATAFRAME
        df = pds.DataFrame(table)
        #
        # GUARDAR EN SQLITE3
        mf.savesqlite3(df)
        #
        # SALVAR LOS DATOS EN UN ARCHIVO JSON.
        df.to_json('data.json')
        #
        # INSERTAR LOS DATOS EN EL HTML
        htmlcontent = mf.insertintoHTML( 'index.html', df )
        return htmlcontent
    except Exception as e:
        htmlcontent = mf.exception_to_string(e)
        htmlcontent = htmlcontent.replace('\n', "<br><br>" )
        htmlcontent = ("Error inesperado, contacte a su proveedor.<br>ERROR: <br><h3 style='background-color:red;'>" + htmlcontent + "</h3>" )
        return htmlcontent
    #
    #
    #
    #
###############################################################################
## CLASE PARA EL SERVIDOR
###############################################################################
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
        ###############################################################################
        ## PUERTO DE LA APLICACION i.e. ("http://localhost:%s/" % port)
        port = 8000
        server = HTTPServer(('', port), WebServerHandler)
        print ("Web Server running on port %s" % port)
        print ("\n\nhttp://localhost:%s/\n\n" % port)
        webbrowser.open_new( "http://localhost:%s/" % port )
        server.serve_forever()
    except KeyboardInterrupt:
        print (" ^C entered, stopping web server....")
        server.socket.close()
        print("FIN")

if __name__ == '__main__':
    main()

