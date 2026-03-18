from django.db import models

# Lab #2: Post 資料表
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

# HW #1: 課程資料表
class Course_table(models.Model):
    Department = models.CharField(max_length=100)
    CourseTitle = models.CharField(max_length=100)
    Instructor = models.CharField(max_length=100)