from rest_framework import viewsets

from cghs_financial.serializers import TagSerializer, ExpenseSerializer
from cghs_financial.models import Tag, Expense
from cghs_financial.filters import ExpenseFilter, TagFilter


class ExpenseViewSet(viewsets.ModelViewSet):

    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return ExpenseFilter(
            self.request.data, queryset=Expense.objects.all()).qs


class TagViewSet(viewsets.ModelViewSet):

    serializer_class = TagSerializer

    def get_queryset(self):
        return TagFilter(self.request.data, queryset=Tag.objects.all()).qs
