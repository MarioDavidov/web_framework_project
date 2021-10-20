from django.urls import path

from weigth.views import WeighListtApiView,WeightDetailsApiView

urlpatterns = [
    path('weight', WeighListtApiView.as_view(), name='weigth list api'),
    path('<int:pk>/', WeightDetailsApiView.as_view(), name='weigth details api'),
]