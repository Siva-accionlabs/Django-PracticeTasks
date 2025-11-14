from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    


# UserCreationForm and UserChangeForm
# reverse vs reverse_lazy:
# when django starts up, it loads and set up URL routes but doesn't execute any view code.
# Class based views are only prepared using as_view(), not run
# Because URLs aren't fully loaded yet, using reverse() at import time can fail- so in class based views,
# You should use reverse_lazy(), which delays URL resolution until it's actually needed at runtime