import math, os
import json 
import hashlib
import sqlite3
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
#################################################################
#################################################################
def insertintoHTML( htmlname, df ):
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
    return incnt
#################################################################
#################################################################
#################################################################
def savesqlite3( df ):
    querycreate = "CREATE TABLE IF NOT EXIST ZINOBE( "
    valuesintable = "("
    for col in df.columns:
        valuesintable += "{0}, ".format(col)
    conn = sqlite3.connect('ZINOBE.db')
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE if not exists stocks
                    (Region text, City_Name text, Languaje text, Time text)''')
    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    # Save (commit) the changes
    conn.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

