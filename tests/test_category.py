import pytest

from product.models import Category


@pytest.mark.django_db
def test_create_category():
    category = Category.objects.create(
        title='Teste',
        slug='teste',
        description='Descrição de teste...',
    )

    assert category.title == 'Teste'
    assert category.slug == 'teste'
    assert category.description == 'Descrição de teste...'
