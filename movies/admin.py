from django.contrib import admin
from .models import Genre, Movie, Review

# 만들었던 모델들을 등록
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Review)
