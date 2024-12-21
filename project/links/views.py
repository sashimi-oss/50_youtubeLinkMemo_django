from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .forms import LinkForm, WatchForm, cateListForm
from .models import Link, Category

def index(request):
  return render(request, 'links/index.html')

def create(request):

  if request.method == 'POST':
    form = LinkForm(request.POST)
    if form.is_valid():
      form.save()

    return redirect('links:index') #まだ未検証

  form = LinkForm()

  #params
  params = {
    'form':form,
  }
  return render(request, 'links/create.html', params)


def watch(request, categoryId = 0):

  if request.method == 'POST':
    form = WatchForm(request.POST)
    if form.is_valid():
      category = form.cleaned_data['category']
      id = category.category_id
    # print(id)
      redirect_url = reverse('links:watch', args=[id])
      return redirect(redirect_url)
    else:
      return redirect('links:watch')
    


  #dbから値を読み込むコード
  if categoryId == 0 or categoryId == 1:
    links = Link.objects.order_by('link_id')
  else:
    links = Link.objects.filter(category_id = categoryId).order_by('link_id')

  form = WatchForm()

  params = {
    'links':links,
    'form':form,
    'categoryId':categoryId,
  }
  return render(request, 'links/watch.html', params)


def cateList(request):
  if request.method == 'POST':
    form = cateListForm(request.POST)
    if form.is_valid():
      form.save()

    return redirect('links:cateList')

  forms = cateListForm()

  category = Category.objects.order_by('category_id')

  params = {
    'forms':forms,
    'categories':category,
  }
  
  return render(request, 'links/cateList.html', params)


def delLink(request, link_id, categoryId):
  if request.method == 'POST':

    link_record = Link.objects.get(pk=link_id)
    # print(link_record, '--------deleteLink-------')
    link_record.delete()

    redirect_url = reverse('links:watch', args=[categoryId])
    return redirect(redirect_url)


def delCate(request, category_id):
  if request.method == 'POST':
    category = Category.objects.filter(category_id=category_id)
    category.delete()

    return redirect('links:cateList')
  
def update(request, link_id):
  if request.method == 'POST':
    
    link = Link.objects.filter(pk=link_id).first()
    form = LinkForm(request.POST, instance=link)
    if form.is_valid():
      form.save()

    return redirect('links:watch')
    
  
  link = Link.objects.filter(pk=link_id).first()
  form = LinkForm(instance=link)

  params = {
      'link':link,
      'form':form,
    }

  return render(request, 'links/update.html', params)