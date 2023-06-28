from django.shortcuts import render

def explore(request):
    return render(request, 'explore.html')

def explore_detial(request):
    return render(request, 'detail.html')