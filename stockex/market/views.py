from django.shortcuts import render
import requests
import json 

# Create your views here.
def index(request):

    #api_request = requests.get("")
    url = "https://api.metaphor.systems/search"

    payload = { "query": "stock exchange" }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-key": "YOUR-API-KEY"
    }

    response = requests.post(url, json=payload, headers=headers)

    #print(response.text)

    #try:
    #    api=json.loads(response.content)
    #except Exception as e:
    #    api="Error, data not loading"

    #return render(request, 'index.html', {'api':api})

    api_data = json.loads(response.content)
    return render(request, 'index.html', {'api': api_data})

