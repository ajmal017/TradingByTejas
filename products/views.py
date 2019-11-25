from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#from venv import hello
from hello import getFinalData

import json
def index(request):
    final = getFinalData()
    print(final)
    return HttpResponse(json.dumps(final))

