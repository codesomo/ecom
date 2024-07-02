from django.db import models
from django.contrib.auth.models import User

# Create your models here.
...
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to ='upload_images/')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.category_name

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=500)
    item_price = models.IntegerField(default=0)
    item_image = models.ImageField(upload_to ='upload_images/')
    is_offer = models.BooleanField(default=False)
    offer_price = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,related_name='item_category', blank=True, null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.item_name

class ShippingAddress(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    landmark = models.CharField(max_length=100)
    pin = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    user = models.ForeignKey(User,related_name='user_shipping_address', blank=True, null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.name) + " - " +str(self.address)

class Cart(models.Model):
    user = models.ForeignKey(User,related_name='user_cart', blank=True, null=True,on_delete=models.SET_NULL)
    item = models.ForeignKey(Item,related_name='cart_item', blank=True, null=True,on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0)
    amount = models.CharField(max_length=10)
    def __str__(self):
        return self.user.username

class Payment(models.Model):
    user = models.ForeignKey(User,related_name='user_payment', blank=True, null=True,on_delete=models.SET_NULL)
    amount = models.IntegerField(default=0)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    payment_mode = models.CharField(max_length=100)
    expected_delivery_date = models.DateTimeField(null=True)
    user = models.ForeignKey(User,related_name='user_order', blank=True, null=True,on_delete=models.SET_NULL)
    total_amount = models.IntegerField(default=0)

    ship_address = models.ForeignKey(ShippingAddress,related_name='order_shipping_address', blank=True, null=True,on_delete=models.SET_NULL)

    payment= models.ForeignKey(Payment,related_name='order_payment', blank=True, null=True,on_delete=models.SET_NULL)
    

    def __str__(self):
        return self.user.username
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='item_order', blank=True, null=True,on_delete=models.SET_NULL)
    # item_id = models.IntegerField(default=0)
    item = models.ForeignKey(Item,related_name='order_items', blank=True, null=True,on_delete=models.SET_NULL)

    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.order.id)
    
