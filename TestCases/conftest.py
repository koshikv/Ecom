from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# =========================================================================================

# it is hook for adding Environment into HTML Reports
def pytestConfigur(config):
    config.metadata['Project Name'] = "Nop Commerce"
    config.metadata['Module Name'] = "Customers"
    config.metadata['tester'] = "koshik"


# hook for modify / delete Environment into HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)

# we are create the fixture to avoid the duplication data in test script as soon as we call the setup method then it
# will automatically tur on th driver pytest_addoption(parser) method will get the value from CLI/hooks.and whatever
# the browser we type it will get from CLI
# setup (fixture) method will decide which browser will launch
# browser method (fixture) will return the browser value to setup method (fixture)
# AssertionError means that the assertion is false, and that’s why the test has failed.
# conftest.py is a special file for pytest where you can add all your test fixtures.
# These fixtures will be visible to all the modules in the same test directory.
# Note: if you are having multiple test packages you can add one conftest.py per package. these files have
# directory scope.
