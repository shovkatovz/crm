from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'company']

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['customer', 'subject', 'note']

from .models import Deal

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['customer', 'title', 'amount', 'status']

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed', 'customer']