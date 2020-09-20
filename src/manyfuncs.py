import math, os
import json 
import hashlib
import sqlite3
#################################################################
#
# REALIZAR PRUEBAS DE LOS MODULOS QUE SE VAN A NECESITAR
# SI NO EXISTEN, SE INSTALAN
def getimports():
    try:
        import requests
        import pandas
    except ImportError as error:
        print("Instalando requests")
        os.system( "pip install requests" )
        print("Instalando pandas")
        os.system( "pip install pandas" )
        try:
            import Requests
            import pandas
            print("Requests y pandas: Instalado !!!")
        except ImportError as error:
            print( "ERROR:" )
            print( error )
            print( "\n\nSOLICITE INFORMACION A SU PROVEEDOR PARA ESTE ERROR" )
            exit(0)
        print("Requests y pandas: IMPORTADO !!!")
#################################################################
def cls():
    clear = lambda:os.system('cls')
    clear()
#################################################################
def get_ulr_response_as_json( url1 ):
    import requests
    x = requests.get(url1)
    y = json.loads(x.text)
    return y
#################################################################
def tosha1( text ):
    h = hashlib.new("sha1", text.encode('utf8') )
    return h.hexdigest().upper()
#################################################################
#################################################################
#################################################################
def insertintoHTML( htmlname, df ):
    # TABLA REGION, City Name... 
    htmltbl = "<tr>\n"
    for col in df.columns:
        htmltbl += "<th scope='col'>{0}</th>\n".format(col)
    htmltbl += "</tr>\n\n"
    for datasiloc in df.iloc:
        htmltbl += "<tr>\n"
        for datas in datasiloc:
            if( "{0}".format(type(datas))=="<class 'numpy.float64'>" ):
                htmltbl += "<td>" + ("{0:.2f} ms".format(datas)) + "</td>\n"
            else:
                htmltbl += "<td>" + ("{0}".format(datas)) + "</td>\n"
        htmltbl += "</tr>\n\n"
    incnt = open( htmlname, "rb", buffering=0).read().decode('utf-8')
    incnt = incnt.replace( "{% tabla de contenido %}", htmltbl )
    #
    # TABLA DE TIEMPOS
    htmltbl  = "<tr>\n<td>{0:.4f}</td>\n".format( df['Time'].sum() )
    htmltbl += "<td>{0}</td>\n".format( df['Time'].mean() )
    htmltbl += "<td>{0}</td>\n".format( df['Time'].min() )
    htmltbl += "<td>{0}</td>\n</tr>\n".format( df['Time'].max() )
    #
    incnt = incnt.replace( "{% tabla de tiempos %}", htmltbl )
    #
    #
    #
    return incnt
#################################################################
#################################################################
#################################################################
def savesqlite3( df ):
    querycreate = "CREATE TABLE IF NOT EXISTS ZINOBE( Region varchar(64), City_Name varchar(64), Languaje varchar(64), Time_in_ms float )" 
    conn = sqlite3.connect('ZINOBE.db')
    c = conn.cursor()
    #
    # DESCOMENTE ESTA SOLICITUD SI QUIERE QUE
    # SE BORRE LA TABLA
    # c.execute( "drop table ZINOBE" )
    #
    # Crear tabla
    c.execute( querycreate )
    # Insertar datos dentro de la tabla
    for datasiloc in df.iloc:
        querydatas = "insert into ZINOBE(Region, City_Name, Languaje, Time_in_ms) VALUES( "
        for datas in datasiloc:
            if( "{0}".format(type(datas))=="<class 'numpy.float64'>" ):
                querydatas += ("{0} );".format(datas))
            else:
                querydatas += ("'{0}', ".format(datas))
        c.execute( querydatas )
    # GUARDAR CAMBIOS
    conn.commit()
    # 
    # CERRAR CONEXION
    conn.close()

