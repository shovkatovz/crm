from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='contacts')
    subject = models.CharField(max_length=200)
    note = models.TextField()
    contact_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.customer.name}"


class Deal(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='deals')
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('new', 'New'), ('won', 'Won'), ('lost', 'Lost')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.customer.name}"


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title