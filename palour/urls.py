from django.urls import path
from . import views

    
urlpatterns = [
    path('',views.phome,name="home"),
    path('gallery/',views.gallery,name="gallery"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),

    path('user/',views.user_reg.as_view(),name="usersignup"),
    path('client/',views.clientreg.as_view(),name="clientsignup"),
    path('login/',views.userlogin.as_view(),name="userlogin"),

    path('ulogin/',views.user_login_page,name="ulogin"),
    
    path('logout/',views.userlogout,name="logout"),
    path('clogout/',views.clientlogout,name="clogout"),

    path('cstatus/',views.client_status,name="cstatus"),

    path('updateprofile/',views.add_p_details.as_view(),name="pdetails"),
    path('plist/',views.parlour_details,name="plist"),

    path('add/',views.addserv.as_view(),name="adds"),
    path('view/',views.service_list,name="list"),
    path('<int:id>/',views.service_del,name="delete"),
    path('edit/<int:id>/',views.edit,name="edit"),

    path('services/<str:val>/',views.servicelist.as_view(), name='slist'),

    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.show_cart,name='showcart'), 
    path('booking/',views.booking_done,name='booking'), 
    path('checkout/',views.checkout.as_view(),name='checkout'), 
    path('paymentdone/', views.payment_done, name='paymentdone'), 

    path('book/',views.booklist,name="blist"),
    path('tasks/<int:id>/', views.update_status, name='update_status'),

    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),


]
