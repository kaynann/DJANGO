from django.shortcuts import render
from .forms import ContatoForm, ProductModelForm
from django.contrib import messages

def index(request):
  return render(request, 'home/index.html')

def contato(request):
  form = ContatoForm(request.POST)

  if str(request.method) == 'POST':
    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      subject = form.cleaned_data['subject']
      message = form.cleaned_data['message']

      print('Mensagem enviada')
      print(f'Nome: { name }')
      print(f'E-mail: { email }')
      print(f'Assunto: { subject }')
      print(f'Mensagem: { message }')

      messages.success(request, 'E-mail enviado com sucesso!')
    else:
      messages.error(request, 'Erro. O e-mail não foi enviado')

  context ={
    'form': form,
  }

  return render(request, 'home/contato.html', context)


def produto(request):
  if str(request.method) == 'POST':
    form = ProductModelForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      messages.success(request, 'Produto cadastrado com sucesso')
      form = ProductModelForm()
    else:
      messages.error(request, 'Erro ao cadastrar produto')
  else:
    form = ProductModelForm()

  context = {
    'form': form
  }

  return render(request, 'home/produto.html', context)