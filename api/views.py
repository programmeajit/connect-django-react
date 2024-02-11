from .models import Student
from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer