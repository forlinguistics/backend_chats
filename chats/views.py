from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')


@require_http_methods(["GET"])
def list_chats(request):
    return JsonResponse({'chats': []})


@require_http_methods(["GET"])
def show_chat(request, chat_id):
    return JsonResponse({'chat_id': chat_id})


@csrf_exempt
@require_http_methods(["POST"])
def create_chat(request):
    return JsonResponse({'status': 200})
# Create your views here.
