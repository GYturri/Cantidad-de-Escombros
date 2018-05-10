# Cantidad de esconbros
import requests
from bs4 import BeautifulSoup
import time

with requests.Session() as c:
    url = 'https://es.ogame.gameforge.com:443/main/login'
    # Aqui pones tu email
    USERNAME = 'XXXXXXX@hotmail.com'
    # Aqui tu password
    PASSWORD = 'XXXXXXXXX'
    # url para el universo BELLATRIX
    UNI = 's154-es.ogame.gameforge.com'
    KID = ''
    login_data = {'kid':KID, 'login':USERNAME, 'pass':PASSWORD, 'uni':UNI, 'next':'https://s153-es.ogame.gameforge.com/game/index.php?page=overview&relogin=1&loginType=email'}
    c.post(url, data=login_data)

urlescombros = 'https://s154-es.ogame.gameforge.com/game/index.php?page=galaxyContent&ajax=1'
cantidad = 0
# Aqui la cantidad minima de escombros que reporte ejm 80.000 sumados metal y cristal
quiero = 80.0
# Aqui tu numero de galaxia
galaxia = 1
# los sistemas solares a evaluar
desde = 60
hasta = 110
for x in range(desde,hasta):
    datos ={'galaxy':galaxia, 'system':x}
    peticion = c.post(urlescombros, data=datos)
    response_json = peticion.json()
    dato = response_json['galaxy']
    soup = BeautifulSoup(dato, 'html.parser')
    g_data = soup.find_all("li",{"class":"debris-content"})
    for i, item in enumerate(g_data):
        valor = item.text.split(" ")
        num = float(valor[1])
        if i % 2 == 0:
            cantidad = num
        else:
            cantidad = cantidad + num
            if cantidad >= quiero:
                print ("Cantidad: %s - Sistema solar: %s" % (cantidad, x))
            cantidad = 0
    time.sleep(2)