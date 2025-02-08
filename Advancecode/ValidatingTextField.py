# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # Set up WebDriver (ensure you have the correct path to your WebDriver)
# driver = webdriver.Chrome()
#
# try:
#     # Navigate to the target website
#     driver.get("https://tutorialsninja.com/demo/")  # Replace with the actual URL
#     driver.maximize_window()
#     time.sleep(1)
#     # Define the expected text
#     expected_text = "Currency"
#     # Locate the element containing the text (adjust locator as needed)
#     actual_text = driver.find_element(By.XPATH, "//*[text()='Currency']" ).text # Replace with appropriate tag or locator
#     # Get the actual text from the element
#     # actual_text = element.text
#     # Validate if the expected text is present
#     assert expected_text in actual_text
#     # , f"Text validation failed. Expected: '{expected_text}', Found: '{actual_text}'"
#     print("Text validation passed!")
#
# finally:
#     # Close the browser
#     driver.quit()
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# # Set up WebDriver
# driver = webdriver.Chrome()
# try:
#     # Navigate to the target website
#     driver.get("https://tutorialsninja.com/demo/")# Replace with the actual URL
#     driver.maximize_window()
#     time.sleep(3)
#     # Define the expected text
#     expected_text = "Currency"
#     # try:
#         # Wait for the element to be present
#     element = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Currency')]"))
#         )
#         # Get the text from the element
#     actual_text = element.text
#         # Check if the text matches
#     if expected_text in actual_text:
#        print("Text validation passed!")
#     else:
#        print("Text is not present.")
# except Exception as e:
#         # Handles cases where the element is not found or an error occurs
#     print("Text is not present.")
#
# finally:
#     # Close the browser
#     driver.quit()
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to the target website
    driver.get("https://tutorialsninja.com/demo/")  # Replace with the actual URL
    driver.maximize_window()
    time.sleep(1)
    # Define the expected text
    expected_text = "Currency1"

    try:
        # Wait for the element to be present
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Currency')]"))
        )
        # Get the text from the element
        actual_text = element.text
        # Use assert for validation
        assert expected_text in actual_text, "Text is not present or does not match the expected text."
        print("Text validation passed!")

    except Exception as e:
        # print("An error occurred:", str(e))
        print("Text is not present.")

finally:
    # Close the browser
    driver.quit()

