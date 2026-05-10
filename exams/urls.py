from django.urls import path
from .views import *

urlpatterns = [
    path('exams/', get_exams),
    path('questions/<int:exam_id>/', get_questions),
    path('submit/<int:exam_id>/', submit_exam),
]