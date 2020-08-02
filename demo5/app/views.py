from django.shortcuts import render,redirect
from app.models import Inmassage


# Create your views here.
def gotoIndex(request):
    return render(request, 'index.html')

def add(request):
    if request.POST:
        name = request.POST.get("name", None)
        habit = request.POST.getlist("habit", None)
        db = Inmassage.objects.create(name=name, habit=",".join(habit))

        return render(request, "add.html",{"msg":"添加成功"})
    else:
        return render(request, "add.html")

def findAll(request):
    db = Inmassage.objects.all()
    return render(request, 'findAll.html', {"sorce":db})

def updater(request, uid):
    if request.POST:
        name = request.POST.get("name", None)
        habit = request.POST.getlist("habit", None)
        Inmassage.objects.filter(uid=uid).update(name=name, habit=",".join(habit))
        return redirect('/app/findAll/')
    else:
        return render(request, "update.html", {"uid":uid})

def delect(request, uid):
    Inmassage.objects.filter(uid=uid).delete()
    return redirect('/app/findAll/')

def findById(request):
    if request.POST:
        uid = request.POST.get("uid", None)
        print(type(uid))
        print(uid)
        sorece = Inmassage.objects.filter(uid=uid)
        return render(request, "findAll.html", {"sorce":sorece})
    else:
        return render(request, "index.html")