import math, os
import json 
import hashlib
#################################################################
def getimports():
    try:
        import requests
        import pandas
    except ImportError as error:
        print( "ERROR:" )
        print( error )
        print("Instalando requests")
        os.system( "pip install requests" )
        os.system( "pip install pandas" )
        print("Requests y pandas: Instalado !!!")
        import Requests
        import pandas
        print("Requests y pandas: IMPORTADO !!!")
#################################################################
def cls():
    clear = lambda:os.system('cls')
    clear()
cls()
#################################################################
def getpath( ):
    pt = os.path.dirname(os.path.abspath(__file__))
    return pt
#################################################################
def get_ulr_response_as_json( url1 ):
    import requests
    import pandas
    x = requests.get(url1)
    y = json.loads(x.text)
    return y
#################################################################
def tosha1( text ):
    h = hashlib.new("sha1", text.encode('utf8') )
    return h.hexdigest().upper()
#################################################################
def insertintoHTML( htmlname, table ):
    htmltbl = ""
    for datas in table:
        htmltbl = htmltbl + "<tr>\n"
        htmltbl = htmltbl + "<td>" + datas['Region'] + "</td>\n"
        htmltbl = htmltbl + "<td>" + datas['City Name'] + "</td>\n"
        htmltbl = htmltbl + "<td>" + datas['Languaje'] + "</td>\n"
        htmltbl = htmltbl + "<td>" + ("{0:.4f}".format(datas['Time'])) + "</td>\n"
        htmltbl = htmltbl + "</tr>\n"
    incnt = open( htmlname, "rb", buffering=0).read().decode('utf-8')
    incnt = incnt.replace( "{% tabla de contenido %}", htmltbl )
    return incnt


