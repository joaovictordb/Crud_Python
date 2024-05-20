from django.shortcuts import render ,redirect
from  app.forms import PessoaForm
from app.models import Pessoa
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Pessoa.objects.filter(nome__icontains=search)
    else:
        data['db'] = Pessoa.objects.all()
    


    #all = Pessoa.objects.all()
    #paginator = Paginator(all, 2)
    #pages = request.GET.get('page')
    #data['db'] = paginator.get_page(pages)
    return render(request,'index.html', data)


def form(request):
    data = {}
    data['form'] = PessoaForm()
    return render(request, 'form.html',data)

def create(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request,pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    return render(request, 'view.html',data)

def edit(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    data['form'] = PessoaForm(instance=data['db'])
    return render(request,'form.html',data)

def update(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    form = PessoaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Pessoa.objects.get(pk=pk)
    db.delete()
    return redirect('home')