
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.employee_form, name='employee_insert'),
    path('<int:pk>/',views.employee_form, name='employee_edit'),
    path('delete/<int:pk>/',views.employee_delete, name='employee_delete'),
    path('list/',views.employee_list,name='employee_list'),
]
