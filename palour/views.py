from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render,HttpResponseRedirect, redirect
from . forms import user_registration,client_reg,userloginform,serv,pardetails
from .models import userdetail,clientdetail,parlour,service,Cart, Payment, booking
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import razorpay
from django.conf import settings
# Create your views here.

def phome(request):
    return render(request,"palour/home.html")

class user_reg(View):
    def get(self,request):
        fm=user_registration()
        return render(request,"palour/user_register.html",locals())
    def post(self,request):
        fm=user_registration(request.POST)
        if fm.is_valid():
             fm.save()
             messages.add_message(request,messages.SUCCESS,"Register sucessfully") 
        else:
            messages.add_message(request,messages.ERROR,"Opps Error Occured")  
        return render(request,"palour/user_register.html",locals())
    
class clientreg(View):
    def get(self,request):
        frm=client_reg()
        return render(request,"palour/clientreg.html",locals())
    def post(self,request):
        frm=client_reg(request.POST)
        if frm.is_valid():
             frm.save()
             messages.add_message(request,messages.SUCCESS,"Registration request as submitted successfully...waiting for approval") 
        else:
            messages.add_message(request,messages.ERROR,"Opps Error Occured") 
        return render(request,"palour/clientreg.html",locals())
    

class userlogin(View):
    def get(self,request):
        ln=userloginform()
        return render(request,"palour/login.html",locals())
    def post(self,request):
        ln=userloginform(request.POST)
        if ln.is_valid():
            unm=ln.cleaned_data["username"]
            pd=ln.cleaned_data["password"]
            sg=ln.cleaned_data["signup_as"] 
            if sg == 'user':
                u=userdetail.objects.filter(username=unm,password=pd)
                if u.exists():
                    request.session['userlg']=True
                    request.session['user']=unm
                    return HttpResponseRedirect('/plist/')
                else:
                    messages.add_message(request,messages.ERROR,"User does not exist")
            else:
                p=clientdetail.objects.filter(username=unm,password=pd,status="accepted")
                if p.exists():
                    request.session['clientlg']=True
                    request.session['client']=unm
                    return redirect('/view/')
                else:
                    messages.add_message(request,messages.ERROR,"User does not exist")
        return render(request,"palour/login.html",locals())
    
class add_p_details(View):
    def get(self,request):
        fm=pardetails()
        return render(request,"palour/parlour_details.html",locals())
    def post(self,request):
        fm=pardetails(request.POST,request.FILES)
        if fm.is_valid():
            username = request.session.get("client")
            parlournameid=clientdetail.objects.get(username=username)
            print(parlournameid)
            addr=fm.cleaned_data['address']
            rt=fm.cleaned_data['rating']
            desc=fm.cleaned_data['description']
            img=fm.cleaned_data['parlour_image']
            reg=parlour(parlour_name=parlournameid,address=addr,rating=rt,description=desc,parlour_image=img)
            reg.save()
            return redirect("/view/")
        else:
            print("invalid")
        return render(request,"palour/parlour_details.html.html",locals())

class addserv(View):
    def get(self,request):
        form=serv()
        return render(request,"palour/add.html",locals())
    def post(self,request):
        form=serv(request.POST,request.FILES)
        if form.is_valid():
            username = request.session.get("client")
            parlournameid=clientdetail.objects.get(username=username)
            sv=form.cleaned_data['servicename']
            img=form.cleaned_data['images']
            desc=form.cleaned_data['description']
            ch=form.cleaned_data['charges']
            dis=form.cleaned_data['discounted_charges']
            reg=service(parlourname=parlournameid,servicename=sv,images=img,description=desc,charges=ch,discounted_charges=dis)
            reg.save()
            return redirect("/view/")
        else:
            print("invalid")
        return render(request,"palour/add.html",locals())

@login_required   
def service_list(request): 
    username = request.session.get("client")
    parlournameid=clientdetail.objects.get(username=username)
    all_service=service.objects.filter(parlourname=parlournameid)
    context={
        'parlournameid':parlournameid,
        'all_service':all_service,
    }
    return render(request,"palour/service_list.html",context)

def booklist(request): 
    username = request.session.get("client")
    parlournameid=clientdetail.objects.get(username=username)
    all_booking=booking.objects.filter(parlourname=parlournameid)
    context={
        'parlournameid':parlournameid,
        'all_booking':all_booking,
    }
    return render(request,"palour/booking_list.html",context)

def edit(request,id):
    if request.method == 'POST':
        servs=service.objects.get(id=id)
        up=serv(request.POST,request.FILES,instance=servs)
        if up.is_valid():
            up.save()
            return redirect("/view/")
    else:
        servs=service.objects.get(id=id)
        up=serv(instance=servs)
    return render(request,"palour/update.html",{'up':up})

def update_status(request, id):
        if request.method == 'POST':
            bk=booking.objects.get(id=id)
            bk.status = request.POST.get('status')
            bk.save()
            return redirect('/book/')
        return render(request, 'palour/bupdate.html', locals())

def service_del(request,id):
    s=service.objects.get(pk=id)
    s.delete()
    return redirect("/view/")

class servicelist(View):
    def get(self,request,val):
        pnm=clientdetail.objects.get(parlourname=val)
        allsv=service.objects.filter(parlourname=pnm)
        return render(request,'palour/pservice.html',locals())

@login_required
def user_login_page(request):
    return render(request,"palour/userlogin.html")

@login_required
def userlogout(request):
    del request.session['userlg']
    return HttpResponseRedirect('/login/')

def clientlogout(request):
    del request.session['clientlg']
    return HttpResponseRedirect('/login/')

def gallery(request):
    return render(request,"palour/gallery.html")

def contact(request):
    return render(request,"palour/contact.html")

def about(request):
    return render(request,"palour/about.html")

def parlour_details(request):
    parlours=parlour.objects.all()
    return render(request, 'palour/parlour_list.html', {'parlours': parlours})

def client_status(request):
    all_clientdetail=clientdetail.objects.all()
    context={
        'all_clientdetail':all_clientdetail
    }
    return render(request,"palour/client_status.html",context)

def add_to_cart(request):
    service_id=request.GET.get('service_id')
    print("service = ",service_id)
    srv=service.objects.get(id=service_id)
    print("request parlor name = ",srv.parlourname)

    user = request.session.get('user')
    usr=userdetail.objects.get(username=user)
    cart=Cart.objects.filter(user=usr)
    print("cart = ",cart)
    flag = 0
    for p in cart:
        print("cart parlor name = ",p.service.parlourname)
        if p.service.parlourname != srv.parlourname:
            flag = 1
    if flag == 1:
        messages.add_message(request,messages.ERROR,"Different Parlor services added in cart, Please remove first")
        print("Error")
        return redirect(f'/services/{srv.parlourname}')

    Cart(user=usr,service=srv).save()
    return redirect("/cart")

def show_cart(request):
    user = request.session.get('user')
    usr=userdetail.objects.get(username=user)
    cart=Cart.objects.filter(user=usr)
    
    amount=0
    for p in cart:
        value=p.quantity * p.service.discounted_charges
        amount=amount + value
    totalamount=amount + 40
    return render(request,'palour/addtocart.html',locals())

class checkout(View):
    def get(self,request):
        user = request.session.get('user')
        usr=userdetail.objects.get(username=user)
        cart_items=Cart.objects.filter(user=usr)
        parlorname = cart_items[0].service.parlourname
        famount=0
        for p in cart_items:
            value=p.quantity * p.service.discounted_charges
            famount=famount + value
            totalamount=famount + 40
        razoramount = int(totalamount * 100)

        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        data = { "amount": razoramount, "currency": "INR", "receipt": "order_rcptid_12"}
        payment_response = client.order.create(data=data)
        order_id = payment_response['id']
        order_status = payment_response['status']
        if order_status == 'created':
            payment = Payment(
                user=usr,
                amount=totalamount,
                razorpay_order_id=order_id,
                razorpay_payment_status = order_status
            )
            payment.save()
        return render(request,'palour/checkout.html',locals())

def payment_done(request):
    order_id=request.GET.get('order_id') 
    payment_id=request.GET.get('payment_id') 
    slot=request.GET.get('slot') 
    parlorname = request.GET.get('parlorname').strip() 
    date = request.GET.get('date') 
    parlorobj = clientdetail.objects.get(parlourname=parlorname)
    print("payment_done : oid = ",order_id," pid = ",payment_id," slot = ",slot," parlorname = ",parlorname)
    # user=request.user 
    user = request.session.get('user')
    usr=userdetail.objects.get(username=user)
    # customer=Customer.objects.get(id=cust_id)
    
    payment=Payment.objects.get(razorpay_order_id=order_id)
    payment.paid = True
    payment.razorpay_payment_id = payment_id
    payment.save()
   
    cart=Cart.objects.filter(user=usr) 
    for c in cart:
        booking(user=usr,parlourname=parlorobj,service=c.service,quantity=c.quantity,booking_date=date,Time_slot=slot,payment=payment).save()
        c.delete()
    return redirect("booking")

def booking_done(request):
    user = request.session.get('user')
    usr=userdetail.objects.get(username=user)
    order_placed=booking.objects.filter(user=usr) 
    print("order placed = ",order_placed)
    return render(request,'palour/booking.html',locals())

def plus_cart(request):
    if request.method == 'GET':
        srv_id=request.GET['service_id']
        user = request.session.get('user')
        usr=userdetail.objects.get(username=user)
        c=Cart.objects.get(Q(service=srv_id)&Q(user=usr))
        c.quantity+=1
        c.save()
        cart=Cart.objects.filter(user=usr)
        # print(srv_id)
        amount=0
        for p in cart:
            value=p.quantity * p.service.discounted_charges
            amount=amount + value
        totalamount=amount + 40
        data={  
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount 
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        srv_id=request.GET['service_id']
        user = request.session.get('user')
        usr=userdetail.objects.get(username=user)
        c=Cart.objects.get(Q(service=srv_id)&Q(user=usr))
        c.quantity-=1
        c.save()
        cart=Cart.objects.filter(user=usr)
        # print(srv_id)
        amount=0
        for p in cart:
            value=p.quantity * p.service.discounted_charges
            amount=amount + value
        totalamount=amount + 40
        data={  
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount 
        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        srv_id=request.GET['service_id']
        user = request.session.get('user')
        usr=userdetail.objects.get(username=user)
        c=Cart.objects.get(Q(service=srv_id)&Q(user=usr))
        c.delete()
        cart=Cart.objects.filter(user=usr)
        # print(srv_id)
        amount=0
        for p in cart:
            value=p.quantity * p.service.discounted_charges
            amount=amount + value
        totalamount=amount + 40
        data={  
            'amount':amount,
            'totalamount':totalamount 
        }
        return JsonResponse(data)
    
