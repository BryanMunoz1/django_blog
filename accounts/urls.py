from django.urls import path 
from .views import SignUpView, Logoutview

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', Logoutview.as_view(), name='logout')
]
