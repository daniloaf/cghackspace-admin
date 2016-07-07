from django.test import TestCase

from cghs_financial.serializers import TagSerializer
from cghs_financial.models import Tag


class TagSerializerTests(TestCase):

    def test__serialize__full_tag__tag_serialized(self):
        # Arrange
        tag_data = {'pk': 1, 'name': 'tag', 'color': '#FFFFFF'}
        tag = Tag(**tag_data)
        # Act
        serializer = TagSerializer(tag)
        # Assert
        self.assertEqual(serializer.data, tag_data)
