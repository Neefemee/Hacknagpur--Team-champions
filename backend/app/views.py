from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from app.serializers import QuestionSerializer, UserSerializer, GroupSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Question, Answer
from rest_framework import authentication, permissions


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionList(APIView):
    """
    View to list all questions in the system.
    """
    def get(self, request, format=None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True, context={'request': request})
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):
    """
    View to question details.
    """
    def get(self, request, pk, format=None):
        question = Question.objects.get(id=pk)
        serializer = QuestionSerializer(question, context={'request': request})
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        question = Question.objects.get(id=pk)
        serializer = QuestionSerializer(question, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        snippet = Question.objects.get(id=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        