
from django.urls import path, include
from onboarding import views

urlpatterns = [
      path('login/', views.login, name='login'),
      path('signup/', views.signup, name='signup')
]