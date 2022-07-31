from rest_framework.response import Response
from rest_framework import status
from pycoingecko import CoinGeckoAPI
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