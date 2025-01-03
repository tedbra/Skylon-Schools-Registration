from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from datetime import datetime

from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import PasswordChangeView, LoginView

from .models import Student
from .forms import StudentForm, SignInForm
from django.contrib.auth.models import User
import logging

# Create your views here.

#Student.objects.all().delete()

#Date of the day very important

current_day = {'current_date': datetime.now()}
print(current_day['current_date'])



#student_exists = Student.objects.filter(pk=14).exists()
#print(student_exists)  # This should return True if the student exists, False otherwise.


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

def HomeView(request):
    return render(request, 'registration.html',{})


class addStudentView(CreateView):
    form_class = StudentForm
    template_name = "registration.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        profiles = Student.objects.all()
        return render(self.request, self.template_name, {'form':form, 'profiles':profiles})

    # def post(self, *args, **kwargs):
    #     if self.request.method == "POST":
    #         form = self.form_class(self.request.POST)
    #         if form.is_valid():
    #             instance = form.save()
    #             return redirect('home') 
    #         else: 
    #             form = StudentForm()
    #             return JsonResponse({'error':form.errors}, status=400) 
    #     return render(self.request, 'registration.html', {'form': form})


    def addStudentViewFine(self, *args, **kwargs):
        if request.method == 'POST':
            form = StudentForm(self.request.POST)
            if form.is_valid():
                item = form.save(commit=False)
                item.registration_agent = self.request.user
                item.save()
                return redirect('home')
            else:
                form = StudentForm()
            return render (self.request, 'registration.html', {'form': form})



    # def post(self, *args, **kwargs):
    #     if self.request.method == "POST":
    #         form = self.form_class(self.request.POST)
    #         if form.is_valid():
    #             instance = form.save()
    #             ser_instance = serializers.serialize('json', [instance, ])
    #             return JsonResponse({'instance':ser_instance}, status=200)
    #         else:
    #             return JsonResponse({'error':form.errors}, status=400)

    #     return JsonResponse({'error':''}, status=400)

class UserSignInView(LoginView):
    form_class = SignInForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

    def get_context_data (self, **kwargs):
        context = super(UserSignInView, self).get_context_data(**kwargs)
        return context

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student-details.html'

    def get_context_data (self, *args,**kwargs):
        context = super(StudentDetailView, self).get_context_data(*args,**kwargs)
        studenten = get_object_or_404(Student, id=self.kwargs['pk'])
        print(studenten)
        context['student'] = studenten
        #print(student_exists)  # This should return True if the student exists, False otherwise.
        return context

class StudentListView(ListView):
    model = Student
    form_class = StudentForm
    context_object_name = 'students'
    template_name = "student-list.html"
    ordering = ['-id']


    def get_context_data(self, *args, **kwargs):
        context = super(StudentListView, self).get_context_data(*args, **kwargs)
        return context



class UpdateStudentView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'update-details.html'    
    #success_url = reverse_lazy('student_list') #We need to return to the 'article-detail' page 

    # def get_object(self, queryset=None):
    #     student_ID = self.kwargs.get('student_ID')
    #     return get_object_or_404(Student, student_ID=student_ID)

    def get_context_data(self, **kwargs):
        context = super(UpdateStudentView, self).get_context_data(**kwargs) 
        print('This is the GIANT ASS CONTEXT')       
        print(context)
        return context

    # def post(self, request, *args, **kwargs):
    #     if self.request.method == "POST":
    #         form = self.form_class(self.request.POST, self.request.FILES)
    #         if form.is_valid():
    #             instance = form.save()
    #             instance.registration_agent = request.user
    #             instance.save()
    #             return redirect('home') 
    #         else: 
    #             form = StudentForm() 
    #     return render(self.request, 'registration.html', {'form': form})


# class StudentDetailView(DetailView):
#     model = Student
#     template_name = 'student_detail.html'

#     def get_object(self, queryset=None):
#         name = self.kwargs.get('name')
#         return get_object_or_404(Student, name=name)







