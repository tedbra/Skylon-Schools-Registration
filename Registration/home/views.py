from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.generic import CreateView, ListView

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, LoginView

from .models import Student
from .forms import StudentForm, SignInForm

# Create your views here.

#Student.objects.all().delete()

def HomeView(request):
    return render(request, 'base.html',{})


class addStudentView(CreateView):
    form_class = StudentForm
    template_name = "registration.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        profiles = Student.objects.all()
        return render(self.request, self.template_name, {'form':form, 'profiles':profiles})

    def post(self, *args, **kwargs):
        if self.request.method == "POST":
            form = self.form_class(self.request.POST, self.request.FILES)
            if form.is_valid():
                instance = form.save()
                return redirect('home') 
            else: 
                form = MyForm() 
        return render(request, 'registration.html', {'form': form})

class UserSignInView(LoginView):
    form_class = SignInForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

    def get_context_data (self, **kwargs):
        postData = super(UserSignInView, self).get_context_data(**kwargs)
        return postData

class studentListView(ListView):
    model = Student
    form_class = StudentForm
    context_object_name = 'students'
    template_name = "student_list.html"