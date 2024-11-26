from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

def index(request):
  return render(request, 'links/index.html')

def create(request):
  #dbに値を書き込む
  return render(request, 'links/create.html')

def watch(request):
  #dbから値を読み込むコード
  return render(request, 'links/watch.html')