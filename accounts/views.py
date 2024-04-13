from .forms import RegistroForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from coolfinance.models import Ativo, Passivo
from .forms import CustomPasswordChangeForm
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid(): 
            form.save()
            # Redirecione para a página de login 
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registration/signup_form.html', {'form': form})
 
class CustomPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('password_change_done')
    success_message = _("Sua senha foi alterada com sucesso!")

    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session['password_changed'] = True  
        return response

def password_change_done(request):
    return render(request, 'registration/password_change_done.html') 
@login_required
def index(request):
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
        'patrimonio_liquido': patrimonio_liquido,}
    return render(request, 'finance/home.html', context)
@login_required
def conta(request):
    return render(request, 'finance/conta.html')
@login_required
def dashboard(request):
    ativos = Ativo.objects.filter(usuario=request.user).order_by('-data')
    passivos = Passivo.objects.filter(usuario=request.user).order_by('-data')

    total_ativos = sum(ativo.valor for ativo in ativos)
    total_passivos = sum(passivo.valor for passivo in passivos)

    patrimonio_liquido = total_ativos - total_passivos
    context = { 
        'patrimonio_liquido': patrimonio_liquido,}
    return render(request, 'finance/painel.html', context)
