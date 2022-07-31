import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import AddEmailForm
from .services import (
    calculate_btc_rate,
    save_user,
    send_email,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@require_http_methods(["GET", "POST"])
def subscribe(request):
    """handler function to subscribe user from browser by sending get request on '/api/subscribe_api' endpoint"""

    if request.method == "GET":
        return render(request, "get_email.html", {"form": AddEmailForm})
    elif request.method == "POST":
        data = {
            "email": request.POST['email']
        }
        response = requests.post("http://0.0.0.0:80/api/subscribe_api", json=data)
        return JsonResponse(response.text, safe=False)


@api_view(["POST"])
def subscribe_api(request):
    """handler of '/api/subscribe_api' endpoint"""

    form = AddEmailForm(request.data)
    resp = save_user(form.data)
    return Response(resp.data, status=resp.status_code)


@api_view(["GET"])
def get_rate(request):
    """handler of '/api/rate' endpoint sending request on '/api/rate_api' one
    and returning result to user in browser"""

    response = requests.get("http://0.0.0.0:80/api/rate_api")
    
    return JsonResponse(response.text, safe=False)


@api_view(["GET"])
def get_rate_api(request):
    """handler of '/api/rate_api' endpoint return actual BTC to UAH rate"""

    try:
        result = calculate_btc_rate()
        return Response(f"1 BTC = {result} UAH", status=status.HTTP_200_OK)
    except:
        return Response("Invalid status value", status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def send_emails(request):
    """handler of '/api/send_emails' endpoint 
    sending request on '/api/send_emails_api' one and returning result to browser"""

    response = requests.get("http://0.0.0.0:80/api/send_emails_api")
    return JsonResponse(response.text, safe=False)


@api_view(["GET"])
def send_emails_api(request):
    """handler of '/api/send_emails_api' endpoint sending emails to all users listed in 'users.txt' file"""

    with open('users.txt') as file:
        lines = [line.rstrip() for line in file]
    file.close()
    for line in lines:
        send_email(line)

    return Response("Emails have been sent!", status=status.HTTP_200_OK)