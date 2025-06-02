from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Count, Sum

from .models import Customer, Contact, Deal, Task
from .forms import CustomerForm, ContactForm, DealForm, TaskForm

# --- LOGIN & LOGOUT ---
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password incorrect')
    return render(request, 'core/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')


# --- DASHBOARD ---
@login_required
def dashboard(request):
    total_customers = Customer.objects.count()
    total_contacts = Contact.objects.count()
    total_deals = Deal.objects.count()
    total_deal_amount = Deal.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    pending_tasks = Task.objects.filter(completed=False).count()

    context = {
        'total_customers': total_customers,
        'total_contacts': total_contacts,
        'total_deals': total_deals,
        'total_deal_amount': total_deal_amount,
        'pending_tasks': pending_tasks,
    }
    return render(request, 'core/dashboard.html', context)


# --- CUSTOMER ---
@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'core/customer_list.html', {'customers': customers})

@login_required
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'core/customer_form.html', {'form': form})

@login_required
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, 'core/customer_form.html', {'form': form})

@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'core/customer_confirm_delete.html', {'customer': customer})


# --- CONTACT ---
@login_required
def contact_list(request):
    contacts = Contact.objects.select_related('customer').all()
    return render(request, 'core/contact_list.html', {'contacts': contacts})

@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'core/contact_form.html', {'form': form})

@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'core/contact_confirm_delete.html', {'contact': contact})


# --- DEAL ---
@login_required
def deal_list(request):
    deals = Deal.objects.select_related('customer').all()
    return render(request, 'core/deal_list.html', {'deals': deals})

@login_required
def deal_create(request):
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deal_list')
    else:
        form = DealForm()
    return render(request, 'core/deal_form.html', {'form': form})

@login_required
def deal_delete(request, pk):
    deal = get_object_or_404(Deal, pk=pk)
    if request.method == 'POST':
        deal.delete()
        return redirect('deal_list')
    return render(request, 'core/deal_confirm_delete.html', {'deal': deal})


# --- TASK ---
@login_required
def task_list(request):
    tasks = Task.objects.select_related('customer').all()
    return render(request, 'core/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'core/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'core/task_confirm_delete.html', {'task': task})