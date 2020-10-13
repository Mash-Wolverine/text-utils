from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    params = {"name":"Manak","title":"Sharma"}
    #return render(request,"home.html",params)
    return render(request,"text_analyser.html",params)
    #return HttpResponse("<h1> Hello You Are On Index Page </h1> ")

def analyzer(request):
    text2 = request.POST.get("text1","default")
    rmvpunc = request.POST.get("removepunc","off")
    fullcaps = request.POST.get("fullcaps","off")
    newlineremover = request.POST.get("newlineremover","off")
    spaceremover = request.POST.get("spaceremover","off")
    charcounter = request.POST.get("charcounter","off")
    #print(text2)
    #print(rmvpunc)
    if (rmvpunc!="on" and fullcaps!="on" and newlineremover!="on" and spaceremover!="on" and charcounter!="on"):
        return HttpResponse("<h1>Please! Select any Operation And Try again</h1>")
    if rmvpunc =="on":
        analyzed_text = ""
        punctuations = '''!()[]{};:'"\,<=+_->./?~@#$%^&*`'''
        for char in text2:
            if char not in punctuations:
                analyzed_text += char
        params = {"purpose":"Remove Punctuations","analyzed_text":analyzed_text}
        text2 = analyzed_text
        #return render(request,"analyze.html",params) 
    if fullcaps == "on":
        analyzed_text=""
        for char in text2:
            analyzed_text += char.upper()
        params = {"purpose":"Changed To Upper Case","analyzed_text":analyzed_text}
        text2 = analyzed_text
        #return render(request,"analyze.html",params) 
    if newlineremover == "on":
        analyzed_text=""
        for char in text2:
            if char !="\n" and char!="\r":
                analyzed_text += char
        params = {"purpose":"New Line Removed","analyzed_text":analyzed_text}
        text2 = analyzed_text
        #return render(request,"analyze.html",params) 
    if spaceremover == "on":
        analyzed_text=""
        for index,char in enumerate(text2):
            if not(text2[index] ==" " and text2[index+1] == " "):
                analyzed_text += char
        params = {"purpose":"All extra Spaces Are Removed","analyzed_text":analyzed_text}
        text2 = analyzed_text
        #return render(request,"analyze.html",params) 
    if charcounter == "on":
        analyzed_text = 0
        for line in text2:
            for words in line:
                analyzed_text +=len(words)
        params = {"purpose":"Total Characters Are: ","analyzed_text":analyzed_text}
        text2 = analyzed_text
        #return render(request,"analyze.html",params) 
    return render(request,"analyze.html",params)
    #HttpResponse("<h1> Hey I'm Mash </h1> Hello You Are On Remove Punctuation page  ")




'''
def removepunc(request):
    text2 = request.GET.get("text1","default")
    print(text2)
    return HttpResponse("<h1> Hey I'm Mash </h1> Hello You Are On Remove Punctuation page  ")

def capitalizefirst(request):
    return HttpResponse("<h1> Hello You Are On Capitalize First page </h1> ")

def newlineremove(request):
    return HttpResponse("<h1> Hello You Are On New line Remove page </h1> ")

def spaceremove(request):
    return HttpResponse("<h1> Hello You Are On Space Remove page </h1> ")
    
def charcount(request):
    return HttpResponse("<h1> Hello You Are On Character Count page </h1> ")

def capitalizefirst(request):
    return HttpResponse("<h1> Hello You Are On Remove Punctuation page </h1> ")
    
def capitalizefirst(request):
    return HttpResponse("<h1> Hello You Are On Remove Punctuation page </h1> ")
'''