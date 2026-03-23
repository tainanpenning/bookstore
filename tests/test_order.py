import pytest

from django.contrib.auth.models import User
from product.models import Product
from product.models import Category
from order.serializers import OrderSerializer


@pytest.mark.django_db
def test_create_order():
    user = User.objects.create(username='test_user')

    category = Category.objects.create(
        title='Teste',
        slug='teste',
    )

    product = Product.objects.create(
        title='Produto',
        price=100,
    )
    product.category.add(category)

    data = {
        'user': user.id,
        'product': [
            {
                'title': 'Produto',
                'price': 100,
                'category': [category.id],
            }
        ],
    }

    serializer = OrderSerializer(data=data)

    assert serializer.is_valid(), f'Erros: {serializer.errors}'
