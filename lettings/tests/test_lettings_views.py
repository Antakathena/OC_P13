from django import urls
import pytest


@pytest.mark.django_db
def test_lettings_index(client):
    temp_url = urls.reverse(f'lettings:lettings_index')
    response = client.get(temp_url)
    content = response.content.decode()
    expected_title = "Lettings"
    assert expected_title in content
    assert response.status_code == 200


@pytest.mark.skip
@pytest.mark.django_db
def test_letting(client, new_letting):
    temp_url = urls.reverse(
        f'lettings:letting', kwargs={
            'pk': new_letting.pk, 'address': new_letting.address
        }
    )
    print(temp_url)
    response = client.get(temp_url)
    assert response.status_code == 200
