from rest_framework import generics
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAdminUser
# from .permissions import IsAdminOrOwner
from exams.serializers import ExamsSerializer
from exams.models import Exams

from rest_framework.views import APIView, Response, status

class ExamsCreateView(generics.CreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminOrOwner]
    
    serializer_class = ExamsSerializer
    """ output_serializer= ExamsSerializer(many=True) """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message":"Exams created sucessfuly"}, status=status.HTTP_201_CREATED, headers=headers)
    
        


class ExamsListView(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer   


class UpdateExamsView(generics.UpdateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminOrOwner]

    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer
    lookup_url_kwarg = "id"    


class DeleteRetriveExamsView(generics.RetrieveDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminOrOwner]
    
    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer
    lookup_url_kwarg = "id"    


