from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("course/",CourseListView.as_view(),name="course_list"),
    # เพิ่ม path ของ view ที่ต้องการ
    path('idsearch/',course_idsearch,name="ids_earch"),
    path('namesearch/',course_namesearch,name="names_search"),
    path('edit<str:pk>',CourseEditView.as_view(),name="edit"),

    path('delete<str:pk>',CourseDeleteView.as_view(),name="delete"),
]
