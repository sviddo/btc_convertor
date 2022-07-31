from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import AddEmailForm
from .services import (
    save_user, 
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests


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
