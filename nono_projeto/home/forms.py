from django import forms
from .models import Produto

class ContatoForm(forms.Form):
  name = forms.CharField(label='Nome')
  email = forms.EmailField(label='E-mail')
  subject = forms.CharField(label='Assunto')
  message = forms.CharField(label='Mensagem', widget=forms.Textarea)

class ProductModelForm(forms.ModelForm):
  class Meta:
    model = Produto
    fields = ['product_name', 'price', 'product_image', 'description']