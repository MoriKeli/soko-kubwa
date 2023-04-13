from django.db import models
from accounts.models import User


class RetailStore(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='Stores/main/imgs/', default='shop.svg')
    description = models.TextField(blank=False)
    mobile_no_1 = models.CharField(max_length=10, blank=False)
    mobile_no_2 = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=50, blank=False)
    service = models.CharField(max_length=50, blank=False)
    opening_hours = models.TimeField(null=False, blank=False)
    closing_hours = models.TimeField(null=False, blank=False)
    working_days = models.CharField(max_length=30, blank=False)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner}'
    
    class Meta:
        ordering = ['owner']
        verbose_name_plural = 'Retail Stores'


class Branches(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    branch = models.ForeignKey(RetailStore, on_delete=models.CASCADE, editable=False)
    location = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=10, blank=False)
    image = models.ImageField(upload_to='Stores/branches/imgs/', default='shop.svg')
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.branch}'
    
    class Meta:
        ordering = ['branch']
        verbose_name_plural = 'Branches'


class Employees(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    employee = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    store = models.OneToOneField(RetailStore, on_delete=models.CASCADE, editable=False)
    branch = models.OneToOneField(Branches, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(default=0, blank=False)
    role = models.CharField(max_length=20, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.employee}'

    class Meta:
        ordering = ['employee', 'store']
        verbose_name_plural = 'Employees'


class Stock(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    store = models.ForeignKey(RetailStore, on_delete=models.CASCADE, editable=False)
    item = models.CharField(max_length=150, blank=False)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    img = models.ImageField(upload_to='Item-pics/', default='')
    price = models.PositiveIntegerField(default=0)
    cost = models.PositiveIntegerField(default=0, editable=False)
    out_of_stock = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.store}'


    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Retail Stores Stocks'


class Transactions(models.Model):
    id = models.CharField(max_length=30, primary_key=True, unique=True, editable=False)
    shop = models.ForeignKey(RetailStore, on_delete=models.CASCADE, editable=False) 
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING, editable=False)
    item = models.CharField(max_length=150, blank=False)
    quantity = models.PositiveIntegerField(default=0, editable=False)
    price = models.PositiveIntegerField(default=0, editable=False)
    cost = models.PositiveIntegerField(default=0, editable=False)
    payment = models.CharField(max_length=5, blank=False)
    bought = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.customer}'

    
    class Meta:
        ordering = ['-bought']
        verbose_name_plural = 'Transactions'

    