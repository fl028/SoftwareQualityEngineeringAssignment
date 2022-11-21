import pytest
from django.test import override_settings

paths = (
    '/',
)

@override_settings(DEBUG=True)
@pytest.mark.django_db()
@pytest.mark.parametrize('path', paths)
def test_xss_patterns(selenium, live_server, settings, xss_pattern, path):
    print("-------------------- " + str(live_server.url) + " ------------------------")
    selenium.get('%s%s' % (live_server.url, path), )
    assert not xss_pattern.succeeded(selenium), xss_pattern.message