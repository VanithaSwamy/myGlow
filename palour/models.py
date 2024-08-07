from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here

class userdetail(models.Model):
    username=models.CharField(max_length=10,unique=True)
    name=models.CharField(max_length=50)
    mobile= PhoneNumberField(unique=True)
    email=models.EmailField()
    password=models.CharField(max_length=15)
    confirmpassword=models.CharField(max_length=15)

    def __str__(self):
        return self.name

class clientdetail(models.Model):
    username=models.CharField(max_length=10,unique=True)
    regno=models.CharField(max_length=12,unique=True)
    parlourname=models.CharField(max_length=50,unique=True)
    mobile= PhoneNumberField(unique=True)
    email=models.EmailField()
    location=models.CharField(max_length=20)
    password=models.CharField(max_length=15)
    confirm_password=models.CharField(max_length=15)
    status_choices=[
        ("pending","pending"),
        ("accepted","accepted"),
        ("rejected","rejected"),
    ]
    status=models.CharField(max_length=20,choices=status_choices,default="pending")

    def __str__(self):
        return str(self.parlourname)
    
class parlour(models.Model):
    parlour_name= models.ForeignKey(clientdetail, on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    rating= models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)])
    description=models.TextField()
    parlour_image=models.ImageField(upload_to='parlour')
    def __str__(self):
        return str(self.parlour_name)
    
class servicemaster(models.Model):
    service_types={
        ("Facial","Facial"),
        ("Haircuts","Haircuts"),
        ("Hair Spa","Hair Spa"),
        ("Hair coloring/Highlights","Hair coloring/Highlights"),
        ("Hair straightening","Hair straightening"),
        ("Hair smoothening","Hair smoothening"),
        ("Hairstyling","Hairstyling"),
        ("Pedicure","Pedicure"),
        ("Manicure","Manicure"),
        ("Threading","Threading"),
        ("Waxing","Waxing"),
        ("Bleach","Bleach"),
        ("Makeup","Makeup"),
        ("Nail art","Nail art"),
    }
    service_name=models.CharField(max_length=50,choices=service_types,unique=True)

    def __str__(self):
        return str(self.service_name)
    
class service(models.Model):
    parlourname=models.ForeignKey(clientdetail,on_delete=models.CASCADE)
    servicename=models.ForeignKey(servicemaster,on_delete=models.CASCADE)
    images=models.ImageField(upload_to='service')
    description=models.TextField()
    charges=models.FloatField(max_length=10)
    discounted_charges=models.FloatField(max_length=10)

    def __str__(self):
        return str(self.servicename)  

class Cart(models.Model):
    user=models.ForeignKey(userdetail,on_delete=models.CASCADE)
    service=models.ForeignKey(service,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.service.discounted_charges
    
class Payment(models.Model):
    user=models.ForeignKey(userdetail,on_delete=models.CASCADE)
    amount=models.FloatField()
    razorpay_order_id=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id=models.CharField(max_length=100,blank=True,null=True)
    paid=models.BooleanField(default=False)


class booking(models.Model):
    user=models.ForeignKey(userdetail,on_delete=models.CASCADE)
    parlourname=models.ForeignKey(clientdetail,on_delete=models.CASCADE)
    service=models.ForeignKey(service,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    booking_date=models.DateField()
    booking_slot={
        ('10:00-11:00','10:00-11:00'),
        ('11:00-12:00','11:00-12:00'),
        ('12:00-13:00','12:00-13:00'),
        ('13:00-14:00','13:00-14:00'),
        ('18:00-19:00','18:00-19:00'),
        ('19:00-20:00','19:00-20:00'),
        ('20:00-21:00','20:00-21:00'),
        ('21:00-22:00','21:00-22:00'),
    }
    Time_slot=models.CharField(max_length=50,choices=booking_slot)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE,default="")

    def __str__(self):
        return f"{self.user} - {self.service}"


    


    
