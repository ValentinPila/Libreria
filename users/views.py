from django.views.generic import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import *

# Create your views here.
class SignUpView(CreateView):
    form_class = CostumUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class PasswordChangeForm(CreateView):
    template_name = 'accounts/password_change_form.html'
    #model = CostumUser
    #fields = "__all__"
    form_class = CostumUserChangePasswordForm

class PasswordChangeDone(TemplateView):
    template_name = 'accounts/password_change_done.html'
    success_url = reverse_lazy('password_done2')