import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def amazon_sign_in(driver, mobile_number, password):
    a = ActionChains(driver)

    # Hover on sign in tab to pop sign in button
    m = driver.find_element(By.XPATH, '//*[@id="nav-link-accountList"]')
    a.move_to_element(m).perform()

    # Click on sign in button
    n = driver.find_element(By.LINK_TEXT, "Sign in")
    a.move_to_element(n).click().perform()

    # Validate sign in page title
    assert "Amazon Sign In" == driver.title, "Failed to validate title"

    # Enter mobile number
    driver.find_element(By.ID, "ap_email").send_keys(mobile_number)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()

    # Wait for 2 seconds
    time.sleep(2)

    # Validate sign in page title
    assert "Amazon Sign In" == driver.title, "Failed to validate title"

    # Enter password
    driver.find_element(By.ID, "ap_password").send_keys(password)
    driver.find_element(By.ID, "signInSubmit").click()

    # Validated sign in
    sign_in_user = driver.find_element(By.XPATH, '//*[@id="nav-link-accountList-nav-line-1"]').text

    return sign_in_user
