import mercadopago
import json
from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory

CLIENT_ID = '1280735590581038'
CLIENT_SECRET = 'hygp27SZgrXEoNzMM8zJ22LxNL6BnkWe'

acess_token = "APP_USR-1280735590581038-112616-0d94a08ce13117d8636fa4d578b22a27-253517767"


sessionid = "123456789"


def payment(req, **kwargs):
  contador= int(request.form['contador'])
  b=1
  contador-=1
  lista = []
  lista.append(request.form['numero_rifa'])
  while int(contador) >= 1:
    contador-=1
    numerolote_rifa2 = request.form['numero_rifa'+str(b)]
    lista.append(numerolote_rifa2)
    b+=1
  

  preference = {
    "items": [
      {
        "id": sessionid,
        "title": "Numero(s) escolhido(s): {}".format(lista),
        "quantity": 1,
        "currency_id": "BRL",
        "unit_price": b*20
      }
    ]
  }

  mp = mercadopago.MP(CLIENT_ID, CLIENT_SECRET)

  preferenceResult = mp.create_preference(preference)

  url = preferenceResult["response"]["init_point"]
    
  return url



def pesquisa_pagamento_pendente(req, **kwargs):
  mp = mercadopago.MP(CLIENT_ID, CLIENT_SECRET)
  filters = {
        "status": "pending",
        "offset": 0,
        "limit": 10
    }

  searchResult = mp.search_payment(filters,0,40)

  lista_id = []
  for i in searchResult['response']['results']:
    lista_id.append(i['id'])
   
  return print(lista_id)


def pesquisa_pagamento_aprovado(req, **kwargs):
  mp = mercadopago.MP(CLIENT_ID, CLIENT_SECRET)
  filters = {
        "status": "approved",
        "offset": 0,
        "limit": 10
    }

  searchResult = mp.search_payment(filters,0,40)

  lista_id = []
  for i in searchResult['response']['results']:
    lista_id.append(i['id'])
   
  return print(lista_id)


  
def pesquisa_pagamento_recusado(req, **kwargs):
  mp = mercadopago.MP(CLIENT_ID, CLIENT_SECRET)
  filters = {
        "status": "cancelled",
        "offset": 0,
        "limit": 10
    }

  searchResult = mp.search_payment(filters,0,40)

  lista_id = []
  for i in searchResult['response']['results']:
    lista_id.append(i['id'])
   
  return print(json.dumps(searchResult, indent=4))




'''
def pesquisa_pagamento(req, **kwargs):
  mp = mercadopago.MP(CLIENT_ID, CLIENT_SECRET)
  id_t = "6eba8648-40e7-40ff-9fb4-cd99edff55b1"
  result = mp.cancel_payment(str(id_t))

  return print(json.dumps(result, indent=4))



def pesquisa_pagamento(req, ** kwargs):
  mp = mercadopago.MP(CLIENT_ID, CLIENT_SECRET)
  id_t = '253517767-8b0b3561-6129-457e-9876-d766b534e1c4'
  preferênciaResult = mp.get_preference(id_t)
  return print(json.dumps(preferênciaResult, indent = 4))'''