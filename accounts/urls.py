from django.urls import path
from accounts.views import login_page, cart, create_page, activate_email, logout_page, orders, clearcart


urlpatterns = [
    path('login/', login_page, name="login"),
    path('create/', create_page, name="create"),
    path('activate/<email_token>', activate_email, name='activate_email'),
    path('logout/', logout_page, name = 'logout'),
    path('cart/', cart, name="cart"),
    path('orders/', orders, name="orders"),
    path('clearcart/', clearcart, name="clearcart"),
]