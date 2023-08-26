from django.urls import path
from .views import LoginView, LogoutView
from .views import UserRegistrationView
from .views import UserProfileView
from .views import UserLoginView

urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('login/', UserLoginView.as_view(), name='login'),
]
