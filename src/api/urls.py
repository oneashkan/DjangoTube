from django.urls import path , include

url_paaterns=[
    path('auth/',include('accounts.urls',namespace='auth')),
]
