from django.urls import include, path
from django.conf.urls import url

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'fixed_deposit', views.FixedDepositViewSet, basename='fd')
router.register(r'bullion', views.BullionViewSet, basename='bullion')

urlpatterns = [
    url('', include(router.urls)),
    url(r"^current_eval$", views.CurrentEvaluation),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]