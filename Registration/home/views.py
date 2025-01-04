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

def slice_rich_text(rich_text, max_lines=2):
  """
  Slices the given rich text content to the specified number of lines.

  Args:
    rich_text: The HTML content of the RichTextArea.
    max_lines: The maximum number of lines to keep.

  Returns:
    The sliced HTML content.
  """
  lines = rich_text.split('<p>')  # Split the content by line breaks (<br>)
  sliced_lines = lines[:max_lines]  # Keep only the first 'max_lines' lines
  return '<p>'.join(sliced_lines)  # Join the lines back together with line breaks

# Example usage:
my_rich_text = "<p>This is the first line.</p><p>This is the second line.</p><p>This is the third line.</p>"
sliced_text = slice_rich_text(my_rich_text, max_lines=3)
print(sliced_text)


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

def HomeView(request):
    return render(request, 'registration.html',{})


class addStudentView(CreateView):
    form_class = StudentForm
    template_name = "registration.html"
    success_url = reverse_lazy('home')

    def get(self, *args, **kwargs):
        form = self.form_class()
        profiles = Student.objects.all()
        return render(self.request, self.template_name, {'form':form, 'profiles':profiles})
    
    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.fields['payment_baba'].disabled = True
    #     return form

    # def post(self, *args, **kwargs):
    #     if self.request.method == "POST":
    #         form = self.form_class(self.request.POST)
    #         if form.is_valid():
    #             massa = self.request.user
    #             instance = form.save()
    #             #self.form_valid(form)
    #         else: 
    #             form = StudentForm()
    #             return JsonResponse({'error':form.errors}, status=400) 
    #     return render(self.request, 'registration.html', {'form': form})

    # def form_valid(self, form):
    #     instance = form.save()

    #     papasara = instance.id
    #     print (papasara)
    #     instance.student_ID = 'SKRRT'        
    #     instance.save()

    #     return super().form_valid(form)

    # def form_valid(self, form):        
    #     #Get the payment data while updating a couple of things
    #     num_list = []
    #     current_date = datetime.now()
    #     yalass = form.cleaned_data.get('student_ID')
    #     print("What is in Payment History: " + str(yalass))   
    #     #form.instance.student_ID = 'SKRRR'    
    #     form.instance.registration_agent = self.request.user
    #     print(instance.id)

    #     num_list.append('--' + str(current_date))
    #     num_list.append(' Updated by: '+ str(form.cleaned_data['registration_agent']))

    #     if form.cleaned_data.get('payment'):            
    #         num_list.append(' Amount: '+ str(form.cleaned_data.get('payment')))
    #         num_list.append(' Paid via: '+ str(form.cleaned_data.get('payment_method')))
    #         num_list.append(' Reference: '+ str(form.cleaned_data.get('reference')))
    #         num_list.append(' For: '+ str(form.cleaned_data.get('term')))
    #     else:
    #         num_list.append('No PAYMENT WAS DONE')    
            
    #     new_entry = ','.join(map(str, num_list))
    #     new_entry_baba = '<p>'+new_entry+'</p>'

    #     print(new_entry_baba)
    #     form.instance.payment_history = new_entry
    #     form.instance.payment_baba= new_entry_baba

    #     form.instance.payment = 0
    #     form.instance.date_updated = current_date

    #     date_de_merde = str(current_date)
    #     form.instance.student_ID = 'SK'+ date_de_merde[2:4] + str(form.cleaned_data.get('id')).zfill(4)
    #     print('********* THE FOREIGN ID IS : ' + str(form.cleaned_data.get('id')))

    #     return super().form_valid(form)

    def form_valid(self, form):        
        #Get the payment data while updating a couple of things
        instance = form.save()
        num_list = []
        current_date = datetime.now()
        yalass = form.cleaned_data.get('student_ID')
        print("What is in Payment History: " + str(yalass))   
        #form.instance.student_ID = 'SKRRR'    
        instance.registration_agent = self.request.user
        print(instance.id)

        num_list.append('--' + str(current_date))
        num_list.append(' Updated by: '+ str(instance.registration_agent))

        if form.cleaned_data.get('payment'):            
            num_list.append(' Amount: '+ str(instance.payment))
            num_list.append(' Paid via: '+ str(instance.payment_method))
            num_list.append(' Reference: '+ str(instance.reference))
            num_list.append(' For: '+ str(instance.term))
        else:
            num_list.append('No PAYMENT WAS DONE')    
            
        new_entry = ','.join(map(str, num_list))
        new_entry_baba = '<p>'+new_entry+'</p>'

        print(new_entry_baba)
        instance.payment_history = new_entry
        instance.payment_baba= new_entry_baba

        instance.payment = 0
        instance.date_updated = current_date

        date_de_merde = str(current_date)
        instance.student_ID = 'SK'+ date_de_merde[2:4] + str(instance.id).zfill(4)
        print('********* THE FOREIGN ID IS : ' + str(instance.id))

        instance.save()

        return super().form_valid(form)


    # def post(self, *args, **kwargs):
    #     if request.method == 'POST':
    #         form = StudentForm(self.request.POST)
    #         if form.is_valid():
    #             item = form.save(commit=False)
    #             item.registration_agent = self.request.user
    #             item.save()
    #             return redirect('home')
    #         else:
    #             form = StudentForm()
    #         return render (self.request, 'registration.html', {'form': form})


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
    success_url = reverse_lazy('student_list') #We need to return to the 'article-detail' page 

    def get_context_data(self, **kwargs):
        context = super(UpdateStudentView, self).get_context_data(**kwargs) 
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['payment_baba'].disabled = True
        return form


    def form_valid(self, form):        
        #Get the payment data while updating a couple of things
        num_list = []
        current_date = datetime.now()
        yalass = form.cleaned_data.get('student_ID')
        print("What is in Payment History" + str(yalass))   
        #form.instance.student_ID = 'SKRRR' 
        form.instance.registration_agent = self.request.user
        print(form.cleaned_data.get('registration_agent'))

        num_list.append('--' + str(current_date))
        num_list.append(' Updated by: '+ str(form.cleaned_data['registration_agent']))

        if form.cleaned_data.get('payment'):            
            num_list.append(' Amount: '+ str(form.cleaned_data.get('payment')))
            num_list.append(' Paid via: '+ str(form.cleaned_data.get('payment_method')))
            num_list.append(' Reference: '+ str(form.cleaned_data.get('reference')))
            num_list.append(' For: '+ str(form.cleaned_data.get('term')))
        else:
            num_list.append('No PAYMENT WAS DONE')    
            
        new_entry = ','.join(map(str, num_list))
        new_entry_baba = '<p>'+new_entry+'</p>'

        tabala = form.cleaned_data.get('payment_history')
        tabala_baba = form.cleaned_data.get('payment_baba')
        print(tabala_baba)
        form.instance.payment_history = new_entry + f'\n{tabala}'
        form.instance.payment_baba= new_entry_baba + tabala_baba

        form.instance.payment = 0
        form.instance.date_updated = current_date   

        return super().form_valid(form)


# class StudentDetailView(DetailView):
#     model = Student
#     template_name = 'student_detail.html'

#     def get_object(self, queryset=None):
#         name = self.kwargs.get('name')
#         return get_object_or_404(Student, name=name)







