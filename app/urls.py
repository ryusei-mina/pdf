from django.urls import path
from .views import PDFUploadView,PDFDetailView,IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('upload/', PDFUploadView.as_view(), name='pdf-upload'),
    path('<int:pk>/', PDFDetailView.as_view(), name='pdf-detail'),
]