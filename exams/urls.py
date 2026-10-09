from django.urls import path
from .views import *

urlpatterns = [
    path('exams/', get_exams),
    path('questions/<int:exam_id>/', get_questions),
    path('exams/count/, get_exam_count'),
    path('submit/<int:exam_id>/', submit_exam),
    path('welcome/', welcome),
    path('health/', health_check),
]