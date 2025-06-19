from django.urls import path
from .views import (
    JoinSchoolView,
    GetJoinedSchoolsView,
    UsersBySchoolLocationView,
    UserProfileByIdView
)

urlpatterns = [
    path('join-school/', JoinSchoolView.as_view()),
    path('my-schools/', GetJoinedSchoolsView.as_view()),
    path('users-by-school/', UsersBySchoolLocationView.as_view()),
    path('user-profile/<int:id>/', UserProfileByIdView.as_view()),
]