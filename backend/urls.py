from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AccidentsChangeView, AccidentsCheckView, ButtonsView, ChangeTypeOfUsersView, DeletingUsersView, UserProfileListCreateView, userProfileDetailView, AccidentsTypeCreateView, AccidentsTypeDetailView

urlpatterns = [
    path("all-profiles", ChangeTypeOfUsersView.as_view(), name="all-profiles"),
    path("profile/<int:pk>", userProfileDetailView.as_view(), name="profile"),
    path("AccidentsType", AccidentsTypeCreateView.as_view(), name="AccidentsType"),
    path("AccidentsType/<int:pk>", AccidentsTypeDetailView.as_view(), name="ChangeAccidentsType"),
    path("ChangeRole/<int:pk>", ChangeTypeOfUsersView.as_view(), name="ChangeRole"),
    path("DeleteUser/<int:pk>", DeletingUsersView.as_view(), name="DeleteUser"),
    path("ChangeRole", ChangeTypeOfUsersView.as_view(), name="ChangeRole"),
    path("Buttons", ButtonsView.as_view(), name="Buttons"),
    path("Accidents", AccidentsCheckView.as_view(), name="Accidents"),
    path("Accidents/<int:pk>", AccidentsChangeView.as_view(), name="ChangeAccidents")
    # path("",include(router.urls))
]