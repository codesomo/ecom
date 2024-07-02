from django.contrib import admin

# Register your models here.
from .models import Category, Item, Cart, ShippingAddress, Payment, Order,OrderItem

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 0 
class OrderAdmin(admin.ModelAdmin):
    list_display = ("get_name","order_date",)

    def get_name(self, obj):
        return obj.user.username
    model = Order
    #list_display = ('id', 'name', 'geom_type')
    inlines = [
        OrderItemAdmin,
    ]
     
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(ShippingAddress)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Payment)