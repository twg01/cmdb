from django.shortcuts import render

def base(request):
  return render(request, 'base.html', context=locals())

def index(request):
  return render(request, 'index.html', context=locals())

def login(request):
  return render(request, 'login.html', context=locals())

def test(request):
  return render(request, 'test/testindex.html', context=locals())
