from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    closing_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Application(models.Model):
    applicant_name = models.CharField(max_length=100)
    applicant_email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name} - {self.vacancy.title}"
