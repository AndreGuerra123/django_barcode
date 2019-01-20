from django.urls import path
from . import views

urlpatterns = [
    path('',views.BarcodeListView.as_view(), name="list"),    
    path('create', views.BarcodeCreateView.as_view(),name="create"),
    path('detail/<pk>', views.BarcodeDetailView.as_view(), name="detail"),
    path('update/<pk>', views.BarcodeUpdateView.as_view(),name="update"),
    path('delete/<pk>',views.BarcodeDeleteView.as_view(),name="delete")
]
