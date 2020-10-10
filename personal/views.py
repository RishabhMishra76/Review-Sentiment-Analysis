from django.http import HttpResponseRedirect
from django.shortcuts import render
import csv, io
from django.contrib import messages
# Create your views here.
from personal.models import Sentence, NameForm
from personal.models import Reviews




def index(request):
    return render(request,'personal/home.html')

def contact(request):
    return render(request,'personal/index.html')

def prediction(request):
    #print(MODEL.summary())
    Text = request.POST.get('Text',False)
    print(Text)
    Sentenceex = Sentence(str(Text))
    predct = Sentenceex.predection()
    print("Prediction is :",float(predct))
    return render(request, 'personal/home.html', {'prediction':  round(float(predct), 2) * 100})

def data_upload(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Please upload a .csv file.')

        data_set = csv_file.read().decode('ISO-8859-1')
        io_string = io.StringIO(data_set)
        next(io_string)
        dele = Reviews.objects.all()
        dele.delete()
        for column in csv.reader(io_string, delimiter=','):
            _, created = Reviews.objects.update_or_create(
                product_name =column[0], 
                rating=column[1], 
                title=column[2], 
                reviewer=column[3], 
                review_text=column[4], 
                Class=column[5],
            )
        context = {
         'reviews': Reviews.objects.all()
        }
        return render(request, 'personal/review_list.html', context)
    else:
        context = {}
        return render(request, 'personal/upload.html', context)
