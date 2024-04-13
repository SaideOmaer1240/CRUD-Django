from django.shortcuts import render, redirect, get_object_or_404
from . forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
 
def index(request):
    return render(request, 'finance/index.html')

#Criar CRUD para model Ativo
def create_ativo(request):
    if request.method == 'POST':
        form = AtivoForm(request.POST)
        if form.is_valid():
            ativo = form.save(commit=False)
            ativo.usuario = request.user
            ativo.save()
            return redirect('balance')
    else:
        form =AtivoForm()
    return render(request, 'finance/create_ativo.html', {'form': form})

def read_ativo(request):
    ativos = Ativo.objects.filter(usuario=request.user).order_by('-data')
    return render(request, 'finance/read_ativo.html', {'ativos':ativos})

def update_ativo(request, ativo_id):
    ativo = get_object_or_404(Ativo, pk=ativo_id)
    if request.method == 'POST':
        ativo_form = AtivoForm(request.POST, instance=ativo)
        if ativo_form.is_valid():
            ativo_form.save()
            return redirect('read_ativo')
    else:
        ativo_form = AtivoForm(instance=ativo)
    
    return render(request, 'finance/update_ativo.html', {'ativo_form':ativo_form})

def delete_activo(request, ativo_id):
    ativo = get_object_or_404(Ativo, pk=ativo_id)
    if request.method == 'POST':
        ativo.delete()
        return redirect('read_ativo')
    return render(request, 'finance/delete_ativo.html', {'ativo': ativo})

# Criar CRUD para models Passivo

def create_passivo(request):
    if request.method == 'POST':
        form_passivo = PassivoForm(request.POST)
        if form_passivo.is_valid():
            passivo = form_passivo.save(commit=False)
            passivo.usuario = request.user
            passivo.save()
            return redirect('balance')
    else:
        form_passivo = PassivoForm(request.POST)
    return render(request, 'finance/create_passivo.html', {'form_passivo':form_passivo})

def read_passivo(request):
    passivos = Passivo.objects.filter(usuario=request.user).order_by('-data')
    return render (request, 'finance/read_passivo.html', {'passivos':passivos})

def update_passivo(request, passivo_id):
    passivo = get_object_or_404(Passivo, pk=passivo_id)

    if request.method == 'POST':
        form_passivo = PassivoForm(request.POST, instance=passivo)
        if form_passivo.is_valid():
            form_passivo.save()
            return redirect('read_passivo')
    else:
        form_passivo = PassivoForm(instance=passivo)
        return render(request, 'finance/update_passivo.html', {'form_passivo':form_passivo})
    
def delete_passivo(request, passivo_id):
    passivo = get_object_or_404(Passivo, pk=passivo_id)
    if request.method == 'POST':
        passivo.delete()
        return redirect('read_passivo')
    return render(request, 'finance/delete_passivo.html', {'passivo': passivo})

def balance(request):
    ativos = Ativo.objects.filter(usuario=request.user).order_by('-data')
    passivos = Passivo.objects.filter(usuario=request.user).order_by('-data')

    total_ativos = sum(ativo.valor for ativo in ativos)
    total_passivos = sum(passivo.valor for passivo in passivos)

    patrimonio_liquido = total_ativos - total_passivos
    # Criar um dicionario para simplficar 
    context = {
        'ativos': ativos,
        'passivos': passivos,
        'total_ativos': total_ativos,
        'total_passivos': total_passivos,
        'patrimonio_liquido': patrimonio_liquido,  
    }
    return render(request, 'finance/home.html', context)
