from rest_framework import generics, permissions
from .models import SchoolLocation
from .serializers import JoinSchoolSerializer, SchoolLocationSerializer, UserSerializer
from accounts.models import CustomUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

class JoinSchoolView(generics.CreateAPIView):
    serializer_class = JoinSchoolSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}

class GetJoinedSchoolsView(generics.ListAPIView):
    serializer_class = SchoolLocationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SchoolLocation.objects.filter(user=self.request.user)

class UsersBySchoolLocationView(APIView):
    def get(self, request):
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')
        if not lat or not lon:
            return Response({"error": "lat and lon are required"}, status=400)
        users = CustomUser.objects.filter(joined_schools__lat=lat, joined_schools__lon=lon).distinct()
        return Response(UserSerializer(users, many=True).data)

class UserProfileByIdView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'