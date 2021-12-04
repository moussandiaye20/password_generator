from django.shortcuts import render
import requests


def index(request):

    return render(request,'base.html')


def generate(request):
    choice = ''
    len = 3
    special ='on'
    if request.method=='POST':
        choice = request.POST.get("drone", "off")
        len = request.POST.get("len", 3)
        special = request.POST.get("special", 'on')


    params={'upper':choice,'special':special, 'length': len}
    response = requests.get('https://passwordwolf.com/api/',params=params).json()[0]['password']

    context = {'password': response}
    print(response)
    return render(request,'password.html',context=context)