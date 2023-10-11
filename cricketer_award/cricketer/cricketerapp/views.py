from django.shortcuts import render, redirect

from cricketerapp.forms import CricketerForm
from cricketerapp.models import Cricketer


# Create your views here.
def index(request):
    cricketer = Cricketer.objects.all()
    context = {
        'cricketer_list': cricketer
    }
    return render(request, 'index.html', context)

def detail(request, cricketer_id):
    cricketer = Cricketer.objects.get(id=cricketer_id)
    return render(request, "detail.html", {'cricketer': cricketer})

def add_cricketer(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        cricketer = Cricketer(name=name, desc=desc, year=year, img=img)
        cricketer.save()
    return render(request, 'add.html')

def update(request, id):
    cricketer=Cricketer.objects.get(id=id)
    form=CricketerForm(request.POST or None,request.FILES,instance=cricketer)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':cricketer})

def delete(request,id):
    if request.method=='POST':
        cricketer=Cricketer.objects.get(id=id)
        cricketer.delete()
        return redirect('/')
    return render(request,'delete.html')