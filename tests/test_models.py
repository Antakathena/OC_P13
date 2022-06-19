import pytest
from profiles import models as profiles
from lettings import models as lettings


@pytest.mark.django_db
def test_address_model_persists():
    new = lettings.Address()
    new.number = 42
    new.street = "Nowhere_Street"
    new.city = "A city"
    new.state = "A state"
    new. zip_code = "99999"
    new.country_iso_code = "SPACE"
    new.save()
    assert new.street == "Nowhere_Street"
    assert lettings.Address.objects.count() > 0


@pytest.mark.django_db
def test_letting_model_persists(new_address):
    new_letting = lettings.Letting()
    new_letting.title = "new_letting"
    new_letting.address = new_address
    old_letting_obj_count = lettings.Letting.objects.filter().count()
    new_letting.save()
    new_letting_obj_count = lettings.Letting.objects.filter().count()
    assert new_letting.title == "new_letting"
    assert old_letting_obj_count < new_letting_obj_count


@pytest.mark.django_db
def test_profile_model_persists(create_test_user):
    new_profile = profiles.Profile()
    new_profile.user = create_test_user
    new_profile.favorite_city = "Madrid"
    new_profile.save()
    assert new_profile.favorite_city == "Madrid"
    assert profiles.Profile.objects.count() > 0
