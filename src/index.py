import manyfuncs  as mf
mf.getimports()

from http.server import BaseHTTPRequestHandler, HTTPServer
import io, os, sqlite3, webbrowser, time, json
import pandas as pds

###############################################################################
## PUERTO DE LA APLICACION
port = 8000
###############################################################################
## URLs de las APIs necesarias.
url1 = 'https://restcountries-v1.p.rapidapi.com/all?rapidapi-key=125c2c22famshe09ed1a643c5231p143e0ajsn061a27ed8f0e'
url2 = 'https://restcountries.eu/rest/v2/all'
###############################################################################
###############################################################################
def procs(ownself):
    ##
    x = mf.get_ulr_response_as_json(url1)
    y = mf.get_ulr_response_as_json(url2)
    ##
    allregions = []
    table = []
    ti = time.perf_counter()
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
    # SALVAR LOS DATOS EN UN ARCHIVO JSON.
    with open('data.json', 'w') as f:json.dump(table, f)
    #
    df = pds.DataFrame(table)
    df.to_json('data.json')
    #print( df.describe() );print('\n')
    #aa = df.mean(axis=0)
    #print( aa );print('\n')
    #print( df['Region'] )
    #
    htmlcontent = mf.insertintoHTML( 'index.html', table, df )
    print( htmlcontent )
    #
    exit(0)
    #
    ownself.wfile.write( htmlcontent.encode('utf8') )
    #
    #
procs(0)
###############################################################################
## CLASE PARA EL SERVIDOR
###############################################################################
class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            procs( self )
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)
def main():
    try:
        server = HTTPServer(('', port), WebServerHandler)
        print ("Web Server running on port %s" % port)
        print ("\n\nhttp://localhost:%s/\n\n" % port)
        webbrowser.open_new( "http://localhost:%s/" % port )
        server.serve_forever()
    except KeyboardInterrupt:
        print (" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
    main()

