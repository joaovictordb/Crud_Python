from django.forms import ModelForm
from app.models import Pessoa

# Create the form class.
class PessoaForm(ModelForm):
     class Meta:
        model = Pessoa
        fields = ['nome', 'email', 'idade']
