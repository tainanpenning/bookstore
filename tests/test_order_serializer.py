import pytest

from django.contrib.auth.models import User
from order.models import Order
from order.serializers import OrderSerializer
from product.models import Product
from product.models import Category


@pytest.mark.django_db
def test_order_total():
    user = User.objects.create(username='test_user')

    category = Category.objects.create(
        title='Teste',
        slug='teste',
    )

    product_01 = Product.objects.create(
        title='p1',
        price=100,
    )
    product_01.category.add(category)

    product_02 = Product.objects.create(
        title='p2',
        price=100,
    )
    product_02.category.add(category)

    order = Order.objects.create(user=user)
    order.product.add(product_01, product_02)

    serializer = OrderSerializer(order)

    assert serializer.data['total'] == 200
