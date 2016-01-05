from rest_framework import serializers

from cghs_financial.models import Tag, Expense


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('pk', 'name', 'color',)


class ExpenseSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Expense
        fields = ('pk', 'description', 'value', 'date', 'tags',)

    def __get_tags_pks(self):
        tags_data = self.initial_data.pop('tags')
        return [tag['pk'] for tag in tags_data]

    def create(self, validated_data):
        expense = Expense(**validated_data)
        expense.save()
        expense.tags = Tag.objects.filter(pk__in=self.__get_tags_pks())
        expense.save()
        return expense

    def update(self, instance, validated_data):
        Expense.objects.filter(pk=instance.pk).update(**validated_data)
        instance = Expense.objects.get(pk=instance.pk)
        instance.tags = Tag.objects.filter(pk__in=self.__get_tags_pks())
        instance.save()
        return instance
