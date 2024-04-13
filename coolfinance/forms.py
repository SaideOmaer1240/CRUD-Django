from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class LoginForm(AuthenticationForm):
    username = forms.CharField(label=_('Nome de usuário'))
    password = forms.CharField(label=_('Senha'), widget=forms.PasswordInput)
    error_messages = {
        'invalid_login' : _(
            'Por favor, insira um nome de usuário e senha corretos.'
        ),
        'inactive':_('Esta conta está inativa.')
    }
class PasswordChange(PasswordChangeForm):
    class Meta:
        model = User
    old_password = forms.CharField(
        label=_("Palavra-Passe antiga"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True}
        ),
    )
    error_messages = {
        'password_incorrect':_(
            'Palavra-passe antiga errada, por favor tente novamente'
        )
      }
    
    def __init__(self, *args, **kwargs):
        super(PasswordChange, self).__init__(*args, **kwargs)
        self.field_order['old_password'].label = "Senha antiga"
        self.field_order['new_password1'].label = "Nova Senha"
        self.field_order['new_password2'].label = "Nova Senha"
        self.field_order['new_password1'].help_text = '' 
        self.field_order['new_password2'].help_text = 'A senha de confirmação deve ser igual a senha nova'
class RegistroForm(UserCreationForm):
   email = forms.EmailField(label='Email')
   class Meta:
       model = User
       fields = ['username', 'email','password1', 'password2']
       help_texts = {
            'username': '',
            'password1': 'Sua senha não pode ser muito semelhante às suas outras informações pessoais. Sua senha deve conter pelo menos 8 caracteres. Sua senha não pode ser uma senha comumente usada. Sua senha não pode ser completamente numérica.',
            'password2': 'Digite a mesma senha de novo para verificação.',
        }
       def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Nome de usuário"
        self.fields['password1'].label = "Senha"
        self.fields['password2'].label = "Confirmação de senha"
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

class AtivoForm(forms.ModelForm):
    class Meta:
        model = Ativo
        fields = ['nome', 'valor']

class PassivoForm(forms.ModelForm):
    class Meta:
        model = Passivo
        fields = ['nome', 'valor']
        