from django.db import models
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    owner = models.ForeignKey(User)
    user = models.ForeignKey( User , on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item_detail', args=[str(self.id)])
    

class User(models.Model):
    
    class Meta:
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', 'phone_number']
        username = models.CharField(max_length=255)
        email = models.CharField(max_length=255)
        password = models.CharField(max_length=255)
        first_name = models.CharField(max_length=255)
        last_name = models.CharField(max_length=255)
        date_joined = models.DateTimeField(auto_now_add=True)
        def __str__(self):
            return self.name