# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloApiView(APIView):
    def get(self, request):
        my_name = request.GET.get('name', None)
        
        if my_name:
            retValue = {}
            retValue['data'] = "Hello " + my_name
            return Response(retValue, status=status.HTTP_200_OK)
        else:
            return Response(
                {"res": "parameter: name is None"},
                status=status.HTTP_400_BAD_REQUEST
            )

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging

logger = logging.getLogger('django')

@api_view(['GET'])
def myhello_api(request):
    my_name = request.GET.get('name', None)
    
    # 這裡確保即使 name 是 None 也能正常串接字串
    log_name = my_name if my_name else "None"
    logger.debug("************** myhello_api: " + my_name)
    
    if my_name:
        return Response({"data": "Hello" + my_name}, status=status.HTTP_200_OK)
    else:
        return Response(
            {"res": "parameter: name is None"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
import json
import logging
from .models import Post, Course_table

logger = logging.getLogger('django')

# =======================
# Lab #2: Post 相關 API
# =======================
@api_view(['GET'])
def list_post(request):
    posts = Post.objects.all().values()
    return JsonResponse(list(posts), safe=False)
    # return Response({"data": json.dumps(
    #     list(posts),
    #     sort_keys=True,
    #     indent=1,
    #     cls=DjangoJSONEncoder
    # )}, status=status.HTTP_200_OK)

@api_view(['GET'])
def add_post(request):
    title = request.GET.get('title', '')
    content = request.GET.get('content', '')
    photo = request.GET.get('photo', '')
    location = request.GET.get('location', '')
    
    if title:
        new_post = Post()
        new_post.title = title
        new_post.content = content
        new_post.photo = photo
        new_post.location = location
        new_post.save()
        return Response({"data": title + " insert!"}, status=status.HTTP_200_OK)
    else:
        return Response({"res": "parameter: title is None"}, status=status.HTTP_400_BAD_REQUEST)

# =======================
# HW #1: Course 相關 API
# =======================
@api_view(['GET'])
def courselist(request):
    courses = Course_table.objects.all().values()
    return JsonResponse(list(courses), safe=False)
    # return Response({"data": json.dumps(
    #     list(courses),
    #     sort_keys=True,
    #     indent=1,
    #     cls=DjangoJSONEncoder
    # )}, status=status.HTTP_200_OK)

@api_view(['GET'])
def addcourse(request):
    department = request.GET.get('Department', '')
    course_title = request.GET.get('CourseTitle', '')
    instructor = request.GET.get('Instructor', '')
    
    if department and course_title and instructor:
        new_course = Course_table()
        new_course.Department = department
        new_course.CourseTitle = course_title
        new_course.Instructor = instructor
        new_course.save()
        return Response({"data": course_title + " insert!"}, status=status.HTTP_200_OK)
    else:
        return Response({"res": "parameters missing"}, status=status.HTTP_400_BAD_REQUEST)