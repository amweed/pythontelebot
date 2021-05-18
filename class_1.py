import json
import requests
from Tok import keys
class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Увы не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Увы не удалось обработать валюту{base}')
        try:
            amount = int(amount)
        except ValueError:
            raise ConvertionException(f'Увы не удалось обработать количество{amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote}&tsyms={base}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
