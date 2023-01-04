
from django.shortcuts import render
from .classes.active import S3activeResponder
from .classes.deactive import S3deactiveResponder
from .classes.s3creator import s3creatorResponder
from .models import MetaDataModel
# Create your views here.#


def OldHome(request):
    return render(request, "../templates/mytemplates/s3metadata.html")

def NewHome(request):
    return render(request,'../templates/mytemplates/index.html',{
        'Name': "Jabril",
    })

def S3active(request):
    #getting all data from MetaDataModel with orm query
    data = MetaDataModel.objects.all()
    return render(request, '../templates/mytemplates/active.html', {
        # 'Active': S3activeResponder,
        'Active': data,
        })

def S3Deactive(request):
    # getting all data from MetaDataModel with orm query
    data = MetaDataModel.objects.all()
    return render(request, '../templates/mytemplates/deactive.html', {
        # 'Deactive': S3deactiveResponder,
        'Deactive': data,
        })

def s3creator(request):
    return render(request,"../templates/mytemplates/downloadPage.html",{
        'S3Accounts' : s3creatorResponder,
    })

