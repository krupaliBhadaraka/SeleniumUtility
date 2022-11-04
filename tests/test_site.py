"""
Amazon sign in test
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utility.utility import amazon_sign_in


@pytest.fixture()
def driver(request):
    """Fixture to create selenium web driver"""
    chrome_options = Options()
    # Enable following commented line to use headless chrome browser
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver.exe')
    driver.get("https://www.amazon.in")
    driver.maximize_window()
    yield driver
    driver.save_screenshot(request.node.name + '.png')
    driver.quit()


def test_title(driver):
    """Test to validate site title"""
    assert "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in" \
           in driver.title, "Failed to validate title"
    print("Title validated successfully")


def test_amazon_sign_in(driver, mobile_number, username, password):
    """Test Amazon sign in functionality"""
    sign_in_user = amazon_sign_in(driver, mobile_number, password)
    assert sign_in_user == f"Hello, {username}"


def test_report_for_failed(driver):
    """Check failed test result into report"""
    assert False
