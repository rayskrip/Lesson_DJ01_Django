from django.http import HttpResponse


def data_view(request):
    return HttpResponse('<h1>Data Page</h1><p>This is the data page content.</p>')


def test_view(request):
    return HttpResponse('<h1>Test Page</h1><p>This is the test page content.</p>')


def index(request):
    return HttpResponse('<h1>Index Page</h1><p>My first project.</p>')


from django.shortcuts import render

# Create your views here.
