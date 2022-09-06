
from django.urls import path
import image_process.views as views

urlpatterns = [
    path('', views.index,name="index"),
    path('face_detection/detect/', views.detect,name="detect"),
]