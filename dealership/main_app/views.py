from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CleaningForm

from .models import Car, Upgrade
# Create your views here.

class Home(LoginView):
    template_name = 'home.html'

@login_required
def car_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', { 'cars': cars})

@login_required
def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    upgrades_car_doesnt_have = Upgrade.objects.exclude(id__in = car.upgrades.all().values_list('id'))
    cleaning_form = CleaningForm()
    return render(request, 'cars/detail.html',{
        'car':car, 
        'cleaning_form': cleaning_form, 
        'upgrades': upgrades_car_doesnt_have
    })

@login_required
def add_cleaning(request, car_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.car_id = car_id
        new_cleaning.save()
    return redirect('car-detail', car_id=car_id)

@login_required
def associate_upgrade(request, car_id, upgrade_id):
    Car.objects.get(id=car_id).upgrades.add(upgrade_id)
    return redirect('car-detail', car_id=car_id)

@login_required
def remove_upgrade(request, car_id, upgrade_id):
    car = Car.objects.get(id=car_id)
    car.upgrades.remove(upgrade_id)
    return redirect('car-detail', car_id=car.id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('car-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = '__all__'
    # success_url = '/cars/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Car
    fields = '__all__'

class CarDelete(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = '/cars/'

class UpgradeCreate(LoginRequiredMixin, CreateView):
    model = Upgrade
    fields = '__all__'

class UpgradeList(LoginRequiredMixin, ListView):
    model = Upgrade

class UpgradeDetail(LoginRequiredMixin, DetailView):
    model = Upgrade

class UpgradeUpdate(LoginRequiredMixin, UpdateView):
    model = Upgrade
    fields = ['name', 'price']

class UpgradeDelete(LoginRequiredMixin, DeleteView):
    model = Upgrade
    success_url = '/upgrades/'

