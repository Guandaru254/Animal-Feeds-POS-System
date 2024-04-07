from django.shortcuts import render, redirect, get_object_or_404
from .models import DairyMealBag
from .forms import DairyMealBagForm
from .models import Client 
from .forms import ClientForm
#from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from django.urls import reverse

#views 

def dairy_meal_bag_list(request):
    dairy_meal_bags = DairyMealBag.objects.all()
    return render(request, 'dairy_meal_bag_list.html', {'dairy_meal_bags': dairy_meal_bags})

def create_dairy_meal_bag(request):
    if request.method == 'POST':
        form = DairyMealBagForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dairy meal bag created successfully!')
            return redirect('dairy_meal_bag_list')
        else:
            messages.error(request, 'Failed to create dairy meal bag. Please check the form.') 
    else:
        form = DairyMealBagForm()
    return render(request, 'create_dairy_meal_bag.html', {'form': form})

def update_dairy_meal_bag(request, pk):
    dairy_meal_bag = get_object_or_404(DairyMealBag, pk=pk)
    if request.method == 'POST':
        form = DairyMealBagForm(request.POST, instance=dairy_meal_bag)
        if form.is_valid():
            form.save()
            return redirect('dairy_meal_bag_list')
    else:
        form = DairyMealBagForm(instance=dairy_meal_bag)
    return render(request, 'update_dairy_meal_bag.html', {'form': form})

def delete_dairy_meal_bag(request, pk):
    dairy_meal_bag = get_object_or_404(DairyMealBag, pk=pk)
    if request.method == 'POST':
        dairy_meal_bag.delete()
        return redirect('dairy_meal_bag_list')
    return render(request, 'delete_dairy_meal_bag.html', {'dairy_meal_bag': dairy_meal_bag})


#CLIENTS VIEWS

def clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients'})

    # Handle form submission for creating a new client
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')

    # Render the clients' information page with client data and form for creating a new client
    form = ClientForm()
    context = {'clients': clients, 'form': form}
    return render(request, 'clients.html', context)

def update_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'update_client.html', {'form': form})

def client_delete(request, client_id):
    # Fetch the client object from the database
    client = get_object_or_404(Client, pk=client_id)

    # Handle POST request to delete the client
    if request.method == 'POST':
        client.delete()
        return redirect('clients')

    # Render confirmation page for deleting the client
    return render(request, 'client_delete.html', {'client': client})