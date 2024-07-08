from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')

def data_view(request):
    return render(request, 'myapp/data.html')

def test_view(request):
    return render(request, 'myapp/test.html')

def about_view(request):
    return render(request, 'myapp/about.html')