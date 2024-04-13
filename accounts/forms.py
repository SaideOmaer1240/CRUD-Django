from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm
 

class LoginForm(AuthenticationForm):
    username = forms.CharField(label=_("Nome de usuário"))
    password = forms.CharField(label=_("Senha"), widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': _(
            "Por favor, insira um nome de usuário e senha corretos. Note que ambos os campos podem ser sensíveis a maiúsculas e minúsculas."
        ),
        'inactive': _("Esta conta está inativa."),
    }

class RegistroForm(UserCreationForm):
    email = forms.EmailField(label="E-mail")
    first_name = forms.CharField(label='Primeiro nome')
    last_name = forms.CharField(label='Último nome')
     
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password1', 'password2']
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

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este e-mail já está registrado. Por favor, use um e-mail diferente.")
        return email
    


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Senha antiga",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True}),
    )
    new_password1 = forms.CharField(
        label="Nova senha",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    new_password2 = forms.CharField(
        label="Confirmar nova senha",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
 
  
