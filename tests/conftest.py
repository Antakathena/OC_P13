# Arrange, Act, Assert / Given, when,then
import pytest
from profiles import models as profiles
from lettings import models as lettings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# We could need fixtures for :
# user
# superuser/staff (for admin UI)
# invalid user
# profile ( = user FK + favorite city)
# adress


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
def new_user_staff(db, new_user_factory):
    return new_user_factory("Test_user", "password", "MyName", is_staff="True")


@pytest.fixture
@pytest.mark.django_db
def test_register_success(self):
    superuser = User.objects.create_superuser(
        username="admin",
        email="admin@admin.com",
        password="admin"
    )
    superuser.save()
    assert User.objects.count() > 0


@pytest.fixture
def user_data():
    return {'username': "test_user",
            'email': "test_user@test_user.com",
            'password': "Testing321"}


@pytest.mark.django_db
@pytest.fixture
def create_test_user(user_data):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data)
    test_user.set_password(user_data.get('password'))
    test_user.save()
    return test_user

# username="test_user",
# email="test_user@test_user.com",
# password="test_user"


@pytest.fixture
def profile_data(create_test_user):
    return {'user': create_test_user,
            'favorite_city': 'Madrid'
            }


@pytest.fixture
def create_test_profile(db, new_user):
    new_profile = profiles.Profile.objects.create(
        user=new_user,
        favorite_city="Madrid"
    )
    return new_profile


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
        test_address = lettings.Address.objects.create(
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
def invalid_address(db, new_address_factory):
    return new_address_factory(zip_code=7885524324134)


@pytest.fixture
def new_letting(db, new_address):
    new_letting = lettings.Letting.objects.create(
        title="awsome_letting",
        adress=new_address
    )
    return new_letting
