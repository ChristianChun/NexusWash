from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MainMenu(models.Model):
    item = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.item


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Service(models.Model):
    TIER_CHOICES = [
        ('Basic', 'Basic'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
    ]

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()  # Time duration for the service
    tier = models.CharField(max_length=10, choices=TIER_CHOICES)
    additional_features = models.TextField(help_text="Enter features separated by commas.")  # Add-ons based on the tier
    picture = models.FileField(upload_to='carWash/static/uploads')

    def __str__(self):
        return f"{self.name} ({self.tier})"

    def save(self, *args, **kwargs):
        # Auto-generate descriptions for tiers based on the base description
        base_description = self.description
        if self.tier == 'Silver':
            self.description = f"{base_description} + Basic Add-ons"
        elif self.tier == 'Gold':
            self.description = f"{base_description} + Silver Add-ons"
        super().save(*args, **kwargs)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    additional_notes = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking for {self.customer_name} on {self.booking_date} at {self.booking_time}"

    def clean(self):
        if Booking.objects.filter(booking_date=self.booking_date, booking_time=self.booking_time).exists():
            raise ValidationError("There is already a booking at this date and time. Please choose a different time.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    picture = models.FileField(upload_to='carWash/static/uploads')

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
