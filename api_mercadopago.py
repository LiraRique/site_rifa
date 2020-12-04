import mercadopago
import json
from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory

CLIENT_ID = '1280735590581038'
CLIENT_SECRET = 'hygp27SZgrXEoNzMM8zJ22LxNL6BnkWe'


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
