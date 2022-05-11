import json
import requests

class Convertor:

    @staticmethod
    def price(base, sum, quantity, key):
        result = 1
        base_key = base
        sym_key = sum
        quantity = quantity
        access_key = key

        try:
            # получение курса валют
            r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={base_key}&tsyms={sym_key}")
            resp = json.loads(r.content)

        except:
            result = "Ошибка соединения"

        # проверка ответа на отсутствие ошибок, соответствие шаблону
        if (len(resp) == 1) and (sym_key in resp.keys()):
            result = resp.get(sym_key) * quantity   # умножение ответа на заданное число
            result = round(result, 3)

        else:
            result = "Ошибка запроса курса валют"

        return result
