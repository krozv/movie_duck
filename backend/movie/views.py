from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Movie
from pprint import pprint
import json
# Create your views here.

def movie_main(request):
  # 현재 상영 중인 영화 데이터 -> 뷰에서 컴포넌트로 처리
  # 인기 영화 데이터 -> 뷰에서 컴포넌트로 처리
  pass

def movie_detail(request, movie_pk):
  
  pass


