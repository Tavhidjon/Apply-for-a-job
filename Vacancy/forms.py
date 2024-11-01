from django import forms
from .models import Category, Vacancy, Application

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'description', 'location', 'category', 'closing_date']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['applicant_name', 'applicant_email', 'resume']
