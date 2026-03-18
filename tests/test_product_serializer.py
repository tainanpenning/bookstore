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
        'category': [category.id],
    }

    serializer = ProductSerializer(data=data)

    assert serializer.is_valid(), f'Erros: {serializer.errors}'

    product = serializer.save()

    assert product.title == data['title']
    assert product.description == data['description']
    assert product.price == data['price']

    serializer = ProductSerializer(product)
    serializer_data = serializer.data

    assert serializer_data['title'] == data['title']
    assert serializer_data['description'] == data['description']
    assert serializer_data['price'] == data['price']
