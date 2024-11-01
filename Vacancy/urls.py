from django.urls import path
from .views import (
    category_list, category_create, category_update, category_delete,
    vacancy_list, vacancy_create, vacancy_update, vacancy_delete,
    application_list
)

urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('categories/create/', category_create, name='category_create'),
    path('categories/update/<int:category_id>/', category_update, name='category_update'),
    path('categories/delete/<int:category_id>/', category_delete, name='category_delete'),
    path('vacancies/', vacancy_list, name='vacancy_list'),
    path('vacancies/create/', vacancy_create, name='vacancy_create'),
    path('vacancies/update/<int:vacancy_id>/', vacancy_update, name='vacancy_update'),
    path('vacancies/delete/<int:vacancy_id>/', vacancy_delete, name='vacancy_delete'),
    path('applications/', application_list, name='application_list'),
]
