from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from cghs_financial.views import ExpenseViewSet, TagViewSet


TAG = 'tag'
EXPENSE = 'expenses'

router = DefaultRouter()
router.register(r'expense', ExpenseViewSet, base_name='expense')
router.register(r'tag', TagViewSet, base_name='tag')


urlpatterns = [
    url(r'^', include(router.urls))
]
