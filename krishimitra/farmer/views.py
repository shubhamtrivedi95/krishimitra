from django.shortcuts import render
from . models import client
from . forms import GetData
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
import requests
from pprint import pprint
# Create your views here.
def post_create(request):
    form = GetData(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return redirect('/done')
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


def show(request):
    stack = client.objects.order_by('id')
    template = loader.get_template('receive.html')
    context = {
        'stack': stack,
    }
    return HttpResponse(template.render(context, request))


def response(request):
    Mo_No=request.GET.get("Mobile")
    resp=client.objects.filter(MobileNo=Mo_No)
    return HttpResponse(resp)


def call(request):
    sid = "krishimitra"
    token = "90514427294a84bf7af8bdf334b6941f467f0800"
    customer_no=request.GET.get("To")
    app_id=str(request.GET.get("AppId"))
    print(app_id)
    if not app_id:
        app_id=170514
    r=requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Calls/connect.json'.format(sid=sid),
                        auth=(sid, token),
                        data={
                             'From': customer_no,
                             'To': "09513886363",
                             'CallerId': "09513886363",
                             'Url': "http://my.exotel.in/exoml/start/{}".format(app_id),
                             'TimeLimit': None,
                             'TimeOut': None,
                             'CallType': "trans",
                             'StatusCallback': None
                        })
    return HttpResponse("<html><body><h4> {a} </h4>\r\n <h5> {b} <h5><body></html>".format(a=r.status_code, b=r.json()))
    # pprint(r.json())
