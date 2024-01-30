from django.shortcuts import render, redirect
from .models import Meeting
from django.contrib import messages
from .forms import MeetingForm

def index(request):
  meetings = Meeting.objects.all()
  return render(request, 'reunioes/index.html', {'meetings': meetings})

def register(request):
  if request.method == 'POST':
    form = MeetingForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      messages.success(request, 'Cadastro realizado com sucesso!')
      form = MeetingForm
    else:
      messages.error(request, 'Erro ao cadastrar')
  else:
    form = MeetingForm
  return render(request, 'reunioes/register.html', {'form': form})

def delete_meeting(request, id):
  meetings = Meeting.objects.get(id=id)
  if request.method == 'POST':
    meetings.delete()
    return redirect('/')
  return render(request, 'reunioes/delete.html')