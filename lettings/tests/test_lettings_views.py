from django import urls
from django.contrib.auth import get_user_model
import pytest


# @pytest.mark.parametrize('param', [
#     'profile_index',
#     'profile',
#     # ('letting_index'),
#     # ('lettings')
# ])
# def test_render_views(client, param):
#     temp_url = urls.reverse(param)
#     resp = client.get(temp_url)
#     assert resp.status_code == 200

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
