from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,'index.html')


def count(request):
    text1 = request.POST['text1']
    text1 = len(text1)

    return render(request,'count.html',{'text1': text1})

def count1(request):
    text2 = request.POST['text2']
    text2 = len(text2.split())
    return render(request,'count1.html',{'text2': text2})
    