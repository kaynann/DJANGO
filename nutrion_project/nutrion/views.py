from django.shortcuts import render, redirect
from .models import Food, Consumed

def index(request):
  if request.method == 'POST':
    consumed_food = request.POST['consumed_food']
    consumption = Food.objects.get(name=consumed_food)
    user = request.user
    consumption = Consumed(user=user, consumed_food=consumption)
    consumption.save()

    foods = Food.objects.all()
  else:
    foods = Food.objects.all()

  food_consumed = Consumed.objects.filter(user=request.user)
 
  return render(request, 'nutrion/index.html', {'foods': foods, 'food_consumed': food_consumed})

def delete_food(request, id):
  consumed_food = Consumed.objects.get(id=id)
  if request.method == 'POST':
    consumed_food.delete()
    return redirect('/')
  return render(request, 'nutrion/delete.html') 