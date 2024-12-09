from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
# Create your views here.
class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'course_list.html'

def course_idsearch(request):
    search = request.GET.get('code','')
    courses = Course.objects.filter(id=search)
    return render(request,'course_search.html',{'courses':courses})

def course_namesearch(request):
    search = request.GET.get('code','')
    courses = Course.objects.filter(name=search)
    return render(request,'course_namesearch.html',{'courses':courses})

class CourseEditView(UpdateView):
    model = Course
    fields = ['name','id']
    template_name = 'course_edit.html'
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('course_list')
    template_name = 'course_delete.html'