from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
def httpresponse(request):
    # request is handled using HttpResponse object
    return HttpResponse(5)

def index(request):
    # Django ORM

    category_list=Category.objects.all()[:4]
    item_list=Item.objects.all()[:4]
    
    return render(request,'home.html',context={"category_list":category_list,"item_list":item_list,"active":"home"})

def crud(request):
    #Django ORM
    category=Category.objects.all()
    return render(request,'base.html', context={"category":category})

def add(request):
    #Django ORM
    
    return render(request,'crud.html', )

def add_handler(request):
    #Django ORM

    if request.method=="POST":
        category_name=request.POST.get("category_name")
        category_description=request.POST.get("category_description")

        Category.objects.create(category_name=category_name,category_description=category_description ,category_image="blank.jpeg")
        
    else:
        print("GET Method---")

    
    return redirect(crud)
def update(request):
    
    category_id=request.GET['category_id']
    #Django ORM

    selected_category=Category.objects.get(pk=category_id)
    
    return render(request,'crud.html',context={"update":True, "selected_category":selected_category} )



def update_handler(request):
    #Django ORM

    if request.method=="POST":
        category_name=request.POST.get("category_name")
        category_description=request.POST.get("category_description")
        category_id=request.POST.get("category_id")
    
        Category.objects.filter(pk=category_id).update(category_name=category_name,category_description=category_description )
        
    else:
        print("GET Method---")

    
    return redirect(crud)




def delete_handler(request):
    category_id=request.GET['category_id']
    #Django ORM
    Category.objects.filter(pk=category_id).delete()
    return redirect(crud)



def item_details(request):
    item_id=request.GET['item_id']
    #Django ORM
    item=Item.objects.get(pk=item_id)
    return render(request,'item_details.html',context={"item":item,"active":"home"} )


def add_to_cart(request):
    if request.method=="POST":
        item_id=request.POST.get("item_id")
        qty=request.POST.get("qty")

        item_data=Item.objects.get(pk=item_id)

        amount=int(item_data.item_price)*int(qty)

        Cart.objects.create(user=request.user,item=item_data,quantity=int(qty),amount=amount)
         
        
    else:
        print("GET Method---")

    
    return redirect(index)


def sign_up_form(request):
    #Django ORM
    return render(request,'sign_up.html' )

def login_form(request):
    #Django ORM
    return render(request,'login.html' )

def sign_up_handler(request):

    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        #Django ORM 
        
        User.objects.create_user(username=username,email=email,password=password)
        return render(request,'login.html' )
    else:

        return redirect(index)
 
 

def login_handler(request):
    
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        #Django ORM 
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

        return redirect(index)
    else:

        return redirect(index)
 

#User.objects.create_user(username='somename', password='somepass')

#user = User.objects.create_user(username='john',email='jlennon@beatles.com',password='glass onion')


def loginHandler(request):
    user = authenticate(username="john", password="glass onion")
    if user is not None:
        login(request, user)
        print("login---")
        print(user.username)
        return redirect(index)


def logout_handler(request):
    logout(request)
    return redirect(index)





from django.core import serializers
from django.http import HttpResponse







def cart_list(request):
    user=request.user
    data=Cart.objects.filter(user=user).count()
    #data = serializers.serialize('json', Cart.objects.filter(user=user).order_by("-id"))
    return HttpResponse({data}, content_type='application/json')
    
def category_details(request):
    category_id=request.GET['category_id']
    #Django ORM
    category_data=Category.objects.get(pk=category_id)

    item_data=Item.objects.filter(category=category_data)

    return render(request,'category_details.html',context={"category":category_data, "item_data":item_data} )

def all_category(request):
  
    #Django ORM
    category_data=Category.objects.all()

   

    return render(request,'all_category.html',context={"category":category_data,"active":"category"} )


def all_items(request):
  
    #Django ORM
    item_list=Item.objects.all()
    return render(request,'all_items.html',context={"item_list":item_list,"active":"items"} )


def all_cart_items(request):
  
    #Django ORM
    cart_list=Cart.objects.filter(user=request.user)
    total_amount=0
    for cart in cart_list:
        total_amount += int(cart.amount)
      


    return render(request,'cart_list.html',context={"cart_list":cart_list,"total_amount":total_amount} )

def delete_cart(request):
    cart_id=request.GET['cart_id']
    #Django ORM
    Cart.objects.filter(pk=cart_id).delete()
    return redirect(all_cart_items)

def shipping_address(request):
  
    #Django ORM
    user = request.user
    username = request.user.username
    email = request.user.email
    cart_lit= Cart.objects.filter(user=user)
    total_amount=0
    for cart in cart_lit:
        total_amount += int(cart.amount)
    check_address=ShippingAddress.objects.filter(user=request.user)
    adress=None
    if len(check_address) > 0:
        adress=True
    else: 
        adress=False
    
    return render(request,'shipping_address.html',context={"address_list":check_address, "is_address":adress, "total_amount":str(total_amount)+"00","email":email,"username":username} )



def add_shipping_address(request):

    if request.method=="POST":
        name=request.POST.get("name")
        address=request.POST.get("address")
        landmark=request.POST.get("landmark")
        pin=request.POST.get("pin")
        phone=request.POST.get("phone")
        #Django ORM 
        
        ShippingAddress.objects.create(name=name,address=address,landmark=landmark,pin=pin,phone=phone,user=request.user)
        return redirect(shipping_address)
    else:

        return redirect(index)
 


def search(request):

    if request.method=="POST":
        search_keyword=request.POST.get("search_keyword")
        #Django ORM 
        seacrh_result=Item.objects.filter(item_name__icontains=search_keyword)
        found=True
        if len(seacrh_result) > 0:
            found=True
        else:
            found=False

        return render(request,'search_result.html', context={"seacrh_result":seacrh_result,"found":found})
    else:

        return redirect(index)
 

def payment_order_handler(request):
    trasaction_id=request.GET['trasaction_id']
    shipping_id=request.GET['shipping_id']
    amount=request.GET['amount']

    user = request.user
    cart_lit= Cart.objects.filter(user=user)
# Payment creation
    payment=Payment.objects.create(user=user,amount=int(amount),transaction_id=trasaction_id)
#order creation
    order=Order.objects.create(payment_mode="Online",user=user,total_amount=amount,ship_address_id=shipping_id,payment=payment)
#order item creation
    
    for cart in cart_lit:
        OrderItem.objects.create(order=order,item=cart.item,quantity=cart.quantity)
    Cart.objects.filter(user=user).delete()
    return redirect(index)


def all_order_list(request):
  
    #Django ORM
    order_list=Order.objects.filter(user=request.user)
   
      


    return render(request,'order_list.html',context={"order_list":order_list} )

 