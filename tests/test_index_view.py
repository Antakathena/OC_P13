from django import urls
from pytest_django.asserts import assertTemplateUsed


def test_index(client):
    temp_url = urls.reverse('index')
    response = client.get(temp_url)
    content = response.content.decode()
    expected_title = "Holiday Homes"
    assert expected_title in content
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")
