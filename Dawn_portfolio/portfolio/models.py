from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150, default='')  # ← add this
    bio = models.TextField(default='')
    age = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    degree = models.CharField(max_length=150, default='')
    school = models.CharField(max_length=100, default='')
    year = models.CharField(max_length=50, default='')

    def __str__(self):
        return f"{self.degree} - {self.school}"


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tools = models.TextField()


    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField()
    github = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    def __str__(self):
        return self.email


class Skill(models.Model):
    skill = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return self.skill
