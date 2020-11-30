import mercadopago
import json

CLIENT_ID = '1280735590581038'
CLIENT_SECRET = 'hygp27SZgrXEoNzMM8zJ22LxNL6BnkWe'


def payment(req, **kwargs):
    preference = {
      "items": [
        {
          "title": "Numero",
          "quantity": 1,
          "currency_id": "BRL",
          "unit_price": 20
        }
      ]
    }

    mp = mercadopago.MP(CLIENT_ID, CLIENT_SECRET)

    preferenceResult = mp.create_preference(preference)

    url = preferenceResult["response"]["init_point"]
    
    return url
