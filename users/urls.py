from django.urls import path 

from .views import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
#    path('accounts/password_change/', PasswordChangeForm.as_view(), name='password_change2'),
  #  path('accounts/password_change/done', PasswordChangeDone.as_view(), name='password_done2'),
]
