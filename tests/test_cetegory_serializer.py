import pytest

from product.serializers import CategorySerializer


@pytest.mark.django_db
def test_category_serializer():
    data = {
        'title': 'Teste',
        'slug': 'teste',
        'description': 'descrição de teste...',
    }

    serializer = CategorySerializer(data=data)

    assert serializer.is_valid(), f'Erros: {serializer.errors}'
