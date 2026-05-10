from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Exam, Question, Result
from .serializers import ExamSerializer, QuestionSerializer
from django.contrib.auth.models import User


@api_view(['GET'])
def get_exams(request):
    exams = Exam.objects.all()
    serializer = ExamSerializer(exams, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_questions(request, exam_id):
    questions = Question.objects.filter(exam_id=exam_id)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def submit_exam(request, exam_id):

    answers = request.data.get('answers')
    username = request.data.get('username')

    questions = Question.objects.filter(exam_id=exam_id)

    score = 0

    for question in questions:
        qid = str(question.id)

        if answers.get(qid) == question.correct_answer:
            score += 1

    student = User.objects.get(username=username)

    Result.objects.create(
        student=student,
        exam_id=exam_id,
        score=score
    )

    return Response({
        "message": "Exam Submitted",
        "score": score
    })