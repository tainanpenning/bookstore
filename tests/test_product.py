import pytest

from product.models import Product


@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(
        title='Título de teste do produto',
        description='Descrição de teste do produto',
        price=999,
    )

    assert product.title == 'Título de teste do produto'
    assert product.description == 'Descrição de teste do produto'
    assert product.price == 999
    assert product.id is not None
