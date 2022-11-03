import pytest


def pytest_addoption(parser):
    parser.addoption("--mobile_number", action="store", default="default mobile_number")
    parser.addoption("--username", action="store", default="default username")
    parser.addoption("--password", action="store")


@pytest.fixture()
def mobile_number(pytestconfig):
    """Fixture to get email from CLI"""
    return pytestconfig.getoption("--mobile_number")


@pytest.fixture()
def username(pytestconfig):
    """Fixture to get username from CLI"""
    return pytestconfig.getoption("--username")


@pytest.fixture()
def password(pytestconfig):
    """Fixture to get password from CLI"""
    return pytestconfig.getoption("--password")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and attach screenshot in html report.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    screen_shot_image = str(item).split(' ')[1].replace('>', '') + '.png'
    if report.when == 'call':
        extra.append(pytest_html.extras.url("https://www.amazon.in"))
        extra.append(pytest_html.extras.image(screen_shot_image))
    report.extra = extra
