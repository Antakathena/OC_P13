from django import urls
import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.fixture
def new_user_factory(db):
    def create_app_user(
        username: str,
        password: str = None,
        first_name: str = "firstname",
        last_name: str = "lastname",
        email: str = "test@test.com",
        is_staff: str = False,
        is_superuser: str = False,
        is_active: str = True,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        return user
    return create_app_user


@pytest.fixture
def new_user(db, new_user_factory):
    return new_user_factory("Test_user", "password", "MyName")


@pytest.fixture
def create_test_profile(db, new_user):
    new_profile = Profile.objects.create(
        user=new_user,
        favorite_city="Madrid"
    )
    return new_profile


@pytest.mark.django_db
def test_profile_index(client):
    temp_url = urls.reverse(f'profiles:profiles_index')
    response = client.get(temp_url)
    content = response.content.decode()
    expected_title = "Profiles"
    assert expected_title in content
    assert response.status_code == 200


# @pytest.mark.skip
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
