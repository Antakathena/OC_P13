from django import urls
import pytest
from lettings.models import Address, Letting


@pytest.fixture
def new_address_factory(db):
    def create_test_address(
        number=42,
        street="Nowhere_Street",
        city="A city",
        state="A state",
        zip_code="99999",
        country_iso_code="SPACE"
    ):
        test_address = Address.objects.create(
            number=number,
            street=street,
            city=city,
            state=state,
            zip_code=zip_code,
            country_iso_code=country_iso_code
        )
        return test_address
    return create_test_address


@pytest.fixture
def new_address(db, new_address_factory):
    return new_address_factory()


@pytest.fixture
def new_letting(db, new_address):
    new_letting = Letting.objects.create(
        title="awsome_letting",
        address=new_address
    )
    return new_letting


@pytest.mark.django_db
def test_lettings_index(client):
    temp_url = urls.reverse(f'lettings:lettings_index')
    response = client.get(temp_url)
    content = response.content.decode()
    expected_title = "Lettings"
    assert expected_title in content
    assert response.status_code == 200


# @pytest.mark.skip
@pytest.mark.django_db
def test_letting(client, new_letting):
    temp_url = urls.reverse(
        f'lettings:letting', kwargs={
            'letting_id': new_letting.id
        }
    )
    # ,'address': new_letting.address
    print(temp_url)
    response = client.get(temp_url)
    assert response.status_code == 200
