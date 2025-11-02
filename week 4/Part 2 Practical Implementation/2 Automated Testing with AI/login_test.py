import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# --- Configuration ---
# Use a publicly available sandbox environment for testing
LOGIN_URL = "https://the-internet.herokuapp.com/login"
# Standard, known credentials for successful test
VALID_USERNAME = "tomsmith"
VALID_PASSWORD = "SuperSecretPassword!"
# Invalid credentials for failed login test
INVALID_USERNAME = "wronguser"
INVALID_PASSWORD = "wrongpassword"

def test_successful_login():
    """
    Tests the scenario where a user successfully logs into the application
    with valid credentials.
    """
    print("="*50)
    print("Starting SUCCESSFUL LOGIN test case...")
    # Initialize the Chrome driver. webdriver_manager automatically downloads
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10) # Set an implicit wait time

    try:
        # 1. Navigate to the login page
        print(f"Navigating to URL: {LOGIN_URL}")
        driver.get(LOGIN_URL)
        driver.maximize_window() # Optional: maximize the window

        # 2. Locate and input username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys(VALID_USERNAME)
        print(f"Entered valid username: {VALID_USERNAME}")

        # 3. Locate and input password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(VALID_PASSWORD)
        print("Entered valid password.")

        # 4. Locate and click the login button
        login_button = driver.find_element(By.CSS_SELECTOR, ".fa.fa-2x.fa-sign-in")
        login_button.click()
        print("Clicked Login button.")

        # --- Assertions (Verification Steps) ---

        # Assertion 1: Verify the success message is displayed
        flash_message = driver.find_element(By.ID, "flash")
        assert "You logged into a secure area!" in flash_message.text
        print("✅ Assertion 1 Passed: Success message found.")

        # Assertion 2: Verify the user is on the secure area page (check for Logout button)
        logout_button = driver.find_element(By.CSS_SELECTOR, ".button.secondary.radius")
        assert "Logout" in logout_button.text
        print("✅ Assertion 2 Passed: Logout button found, indicating secure area.")

        # Pause to visually observe the result (remove in production code)
        time.sleep(1)

        print("\nTest finished successfully: User logged in and secure area loaded.")

    except NoSuchElementException as e:
        print(f"❌ Test Failed: Could not find required element on the page.")
        print(f"Error details: {e}")
        assert False, f"Test failed due to missing element: {e}"
    except AssertionError as e:
        print(f"❌ Test Failed: An assertion check failed.")
        print(f"Error details: {e}")
        assert False, f"Test failed: {e}"
    finally:
        # 5. Teardown: Close the browser
        print("Closing the browser.")
        driver.quit()

def test_failed_login():
    """
    Tests the scenario where a user fails to log into the application
    with invalid credentials.
    """
    print("\n" + "="*50)
    print("Starting FAILED LOGIN test case...")
    # Initialize a new driver session
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)

    try:
        # 1. Navigate to the login page
        print(f"Navigating to URL: {LOGIN_URL}")
        driver.get(LOGIN_URL)
        driver.maximize_window()

        # 2. Locate and input INVALID username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys(INVALID_USERNAME)
        print(f"Entered invalid username: {INVALID_USERNAME}")

        # 3. Locate and input INVALID password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(INVALID_PASSWORD)
        print("Entered invalid password.")

        # 4. Locate and click the login button
        login_button = driver.find_element(By.CSS_SELECTOR, ".fa.fa-2x.fa-sign-in")
        login_button.click()
        print("Clicked Login button.")

        # --- Assertions (Verification Steps) ---

        # Assertion 1: Verify the failure message is displayed
        flash_message = driver.find_element(By.ID, "flash")
        expected_error_text = "Your username is invalid!"
        assert expected_error_text in flash_message.text
        print(f"✅ Assertion 1 Passed: Failure message found: '{expected_error_text}'")

        # Assertion 2: Verify the user is NOT redirected to the secure page
        try:
            # If the Logout button is found, the test should fail unexpectedly
            driver.find_element(By.CSS_SELECTOR, ".button.secondary.radius")
            assert False, "❌ Assertion 2 Failed: Logout button was found, implying successful login."
        except NoSuchElementException:
            # This is the expected behavior for a failed login
            print("✅ Assertion 2 Passed: Logout button was NOT found (correctly failed to log in).")

        # Pause to visually observe the result (remove in production code)
        time.sleep(1)

        print("\nTest finished successfully: User failed to log in and received the correct error message.")

    except NoSuchElementException as e:
        print(f"❌ Test Failed: Could not find required element on the page.")
        print(f"Error details: {e}")
        assert False, f"Test failed due to missing element: {e}"
    except AssertionError as e:
        print(f"❌ Test Failed: An assertion check failed.")
        print(f"Error details: {e}")
        assert False, f"Test failed: {e}"
    finally:
        # 5. Teardown: Close the browser
        print("Closing the browser.")
        driver.quit()


if __name__ == "__main__":
    test_successful_login()
    test_failed_login()


