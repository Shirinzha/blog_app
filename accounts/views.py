from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView): #username password password2
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
