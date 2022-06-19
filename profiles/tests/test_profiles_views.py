from django import urls
import pytest


@pytest.mark.django_db
def test_profile_index(client):
    temp_url = urls.reverse(f'profiles:profiles_index')
    response = client.get(temp_url)
    content = response.content.decode()
    expected_title = "Profiles"
    assert expected_title in content
    assert response.status_code == 200


@pytest.mark.skip
@pytest.mark.django_db
def test_profile(client, create_test_profile):
    user = create_test_profile.user
    print(user)
    username = user.username
    print(user.username)
    temp_url = urls.reverse(f'profiles:profile', kwargs={'username': username})
    print(temp_url)
    response = client.get(temp_url)
    assert response.status_code == 200
