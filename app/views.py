from django.http import HttpResponse

from django.shortcuts import render
# Create your views here.
from .models import Dht

def home(request):
    return render(request, 'home.html')

def dht11(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'temperature.html', s)


def dht12(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'graphe.html', s)

def exp_csv(request):
    obj = Dht.object.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filenames=DHT.csv'
    writer = csv.writer(response)
    writer.writerow(['ID',   'Temp',   'DT'])

    studs = obj.values_list('id', 'temp', 'dt')[len(obj)-36:len(obj)]
    for std in studs:
        writer.writerow(std)
    return response





