import pytest

from product.models.category import Category
from product.serializers import ProductSerializer


@pytest.mark.django_db
def test_product_serializer():
    category = Category.objects.create(
        title='Teste',
        slug='teste',
    )

    data = {
        'title': 'Teste serializer',
        'description': 'Testando o serializer...',
        'price': 999,
        'categories_id': [category.id],
    }

    serializer = ProductSerializer(data=data)

    assert serializer.is_valid(), f'Erros: {serializer.errors}'
