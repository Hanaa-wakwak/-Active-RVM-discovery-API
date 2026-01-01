from django.urls import path
from .views import ActiveRVMListAPIView

urlpatterns = [
    path("rvm/active/", ActiveRVMListAPIView.as_view(), name="active-rvms"),
]
