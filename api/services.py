from rest_framework.response import Response
from rest_framework import status
from mailjet_rest import Client
from pycoingecko import CoinGeckoAPI


api_key = '4a883aaef27f79839ef4993374d9722b'
api_secret = '8d247d0eb16fc58793d75f14a4571b0a'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
cg = CoinGeckoAPI()


def save_user(data):
    with open('users.txt') as file:
        lines = [line.rstrip() for line in file]
    file.close()

    if data['email'] in lines:
        return Response("Email is already registered!", status=status.HTTP_400_BAD_REQUEST)
    else:
        with open("users.txt", "a") as file:
            file.write("\n")
            file.write(data['email'])
        file.close()
        return Response("Email has been successfully registered!", status=status.HTTP_200_OK)


def calculate_btc_rate():
    return cg.get_price(ids='bitcoin', vs_currencies='uah')['bitcoin']['uah']


def send_email(email_to_send):
    data = {
    'Messages': [
        {
        "From": {
            "Email": "btcconvertor@gmail.com",
            "Name": "BTC convertor"
        },
        "To": [
            {
            "Email": f"{email_to_send}",
            "Name": "You"
            }
        ],
        "Subject": "BTC to UAH",
        "TextPart": "Greetings from BTC convertor!",
        "HTMLPart": f"<h3>1 BTC = {calculate_btc_rate()} UAH</h3>"
        }
    ]
    }
    mailjet.send.create(data=data)
