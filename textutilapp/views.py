from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def analyze(request):
    # get the text
    djtext=request.GET.get('text','default')

    #check checkbox value
    removepunc=request.GET.get('removepunc','off')
    capitalize = request.GET.get('capitalize','off')
    spaceremove = request.GET.get('spaceremove','off')
    extraspaceremove = request.GET.get('extraspaceremove', 'off')
    newlineremove = request.GET.get('newlineremove','off')
    charcount = request.GET.get('charcount', 'off')

    # if checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzetext=""
        for char in djtext:
            if char not in punctuations:
                analyzetext=analyzetext+char

        params={ "purpose": "Remove punctuation", "analyzed": analyzetext}
        return render(request,"analyze.html",params)


    elif capitalize == "on":
        analyzetext=""
        for char in djtext:
            analyzetext=analyzetext+char.upper()
        params = {"purpose": "Capitalize The string", "analyzed": analyzetext}
        return render(request,"analyze.html",params)


    elif spaceremove == "on":
        analyzetext=""
        for char in djtext:
            if char!=" ":
                analyzetext=analyzetext+char
        params = {"purpose": "Space Remove", "analyzed": analyzetext}
        return render(request,"analyze.html",params)


    elif extraspaceremove == "on":
        analyzetext=""
        for i in range(len(djtext)):
            if not(djtext[i]==" " and djtext[i+1]== " "):
                analyzetext=analyzetext+djtext[i]

        params = {"purpose": " Extra Space Remove", "analyzed": analyzetext}
        return render(request,"analyze.html",params)



    elif newlineremove == "on":
        analyzetext=""
        for char in djtext:
            if char != "\n":
                analyzetext=analyzetext+char

        params = {"purpose": "New line remove", "analyzed": analyzetext}
        return render (request,"analyze.html",params)


    elif charcount == "on":
        analyzetext=len(djtext)
        params = {"purpose": "character  count", "analyzed": analyzetext}
        return render (request,"analyze.html",params)

    else:
        return HttpResponse("No  given option was selected !!")

# def removepunc(request):
#
#
#     return HttpResponse("remove punc")
#
# def capitalize(request):
#     return HttpResponse("capitalize")
#
# def spaceremove(request):
#     return HttpResponse("space is removed")
#
# def newlineremove(request):
#     return HttpResponse("new line is removed")
#
# def charcount(request):
#     return HttpResponse("character count")
