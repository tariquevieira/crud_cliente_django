from django.shortcuts import render,redirect,get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.



def lista_de_clientes(request):
    clientes = Cliente.objects.all().order_by('-id')
    queryset = request.GET.get('q')
    if queryset:
        clientes = Cliente.objects.filter(
            Q(nome__icontains=queryset)|
            Q(email__icontains=queryset)|
            Q(cpf__icontains=queryset)
   
            )
    paginator = Paginator(clientes, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    clientes = paginator.get_page(page)
    return render(request,"clientes/lista_de_clientes.html",{'clientes':clientes})



def adicionar_cliente(request):
    form = ClienteForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = ClienteForm()
        return redirect('lista_de_clientes')

    return render(request,"clientes/adicionar_cliente.html",{'form':form})



def editar_cliente(request,id=None):
    cliente = get_object_or_404(Cliente,id=id)
    form = ClienteForm(request.POST or None,instance=cliente)
    if form.is_valid():
        obj = form.save()
        obj.save()
        return redirect('lista_de_clientes')
    return render(request,"clientes/editar_cliente.html",{'form':form})

def remover_Cliente(request,id=None):
    cliente = get_object_or_404(Cliente,id=id)
    if request.method == "POST":
        cliente.delete()
        return redirect('lista_de_clientes')
    return render(request,"clientes/remover_cliente.html",{'cliente':cliente})

