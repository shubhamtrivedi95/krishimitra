from django.shortcuts import render
from . models import client
from . forms import GetData
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.
def post_create(request):
    form = GetData(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return redirect('/done')
       # client.objects.filter(TokenNo=request.POST.get("TokenNo")).update(Enable=1)
    context={
        "form":form ,
    }
    return render(request,'page.html',context)
def on(request):
    From=request.GET.get("CallFrom")
    print(From)
    client.objects.filter(MobileNo=From).update(Enable=1)
    return HttpResponse("<h2> {f} </h2>".format(f=From))

def off(request):
    From=request.GET.get("CallFrom")
    print(From)
    client.objects.filter(MobileNo=From).update(Enable=0)
    return HttpResponse("<h2> {f} </h2>".format(f=From))

def done(request):
    return HttpResponse("<h2> Request Accepted.</h2>")
def welcome(request):
    return HttpResponse("<h2>Krishimitra </h2>")