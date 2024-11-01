from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Vacancy, Application
from .forms import CategoryForm, VacancyForm, ApplicationForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def category_update(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def category_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy_list.html', {'vacancies': vacancies})

def vacancy_create(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
    else:
        form = VacancyForm()
    return render(request, 'vacancy_form.html', {'form': form})

def vacancy_update(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    if request.method == 'POST':
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
    else:
        form = VacancyForm(instance=vacancy)
    return render(request, 'vacancy_form.html', {'form': form})

def vacancy_delete(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    if request.method == 'POST':
        vacancy.delete()
        return redirect('vacancy_list')
    return render(request, 'vacancy_confirm_delete.html', {'vacancy': vacancy})

def application_list(request):
    applications = Application.objects.all()
    return render(request, 'application_list.html', {'applications': applications})
