import django_filters

from models import Expense, Tag


class ExpenseFilter(django_filters.FilterSet):

    year = django_filters.MethodFilter()
    month = django_filters.MethodFilter()
    tags = django_filters.MethodFilter()

    class Meta:
        model = Expense
        fields = ['year', 'month']

    def filter_year(self, queryset, value):
        return queryset.filter(date__year=value)

    def filter_month(self, queryset, value):
        return queryset.filter(date__month=value)


class TagFilter(django_filters.FilterSet):

    class Meta:
        model = Tag
        fields = ['name', 'color']
