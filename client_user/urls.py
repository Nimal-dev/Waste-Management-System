from django.urls import path
from . import views

urlpatterns = [
    path('client_home/', views.client_homepage, name='client_homepage'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('viewagentclient/', views.viewAgentClient, name='view-agent-client'),
    path('viewfinesclient/', views.viewFinesClient, name='view-fines-user'),
    path('create-razorpay-order/<int:fine_id>/', views.create_razorpay_order, name='create_razorpay_order'),
    path('razorpay-payment-callback/<int:fineid>', views.razorpay_payment_callback, name='razorpay_payment_callback'),
]