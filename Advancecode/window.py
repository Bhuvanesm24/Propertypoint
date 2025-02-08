from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("https://demo.automationtesting.in/Windows.html")
# driver.find_element(By.XPATH, "//button[text()='    click   ']").click()
# time.sleep(2)
# # Open additional windows for demonstration purposes
# driver.execute_script("window.open('https://www.google.com', '_blank');")
# time.sleep(1)
# driver.execute_script("window.open('https://www.bing.com', '_blank');")
# time.sleep(1)
# driver.execute_script("window.open('https://www.yahoo.com', '_blank');")
# time.sleep(1)
#
# # Get all window handles
# window_handles = driver.window_handles
# print(f"Total windows: {len(window_handles)}")
#
# # Iterate through each window
# for index, handle in enumerate(window_handles):
#     # Switch to the window
#     driver.switch_to.window(handle)
#     print(f"Switched to window {index + 1}: {driver.title}")
#
#     # Perform actions on the window
#     print(f"Window {index + 1} URL: {driver.current_url}")
#     time.sleep(2)
#
# # Close all windows
# driver.quit()'
# driver.get("https://demo.automationtesting.in/Windows.html")
# time.sleep(2)
# parent_window = driver.current_window_handle
# print("Nmae of parent window - ", parent_window)
# driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()
# time.sleep(2)
# child_window = driver.window_handles
# print("Nmae of parent window - ", child_window)
#
# for child in child_window:
#     print(child)
#     if parent_window != child_window:
#         driver.switch_to.window(child)
#         driver.find_element(By.XPATH, "//a[normalize-space()='4.28.1 (January 23, 2024)']").click()
#         print(driver.title)
#         time.sleep(5)

# Step 2: Open the LetCode website
driver.get("https://letcode.in/windows")
print(f"Main window title: {driver.title}")

# Step 3: Save the main window handle
main_window = driver.current_window_handle
print(f"Main window handle: {main_window}")

# Step 4: Click the button to open new tabs/windows
driver.find_element(By.XPATH, "//button[@id='multi']").click()
time.sleep(3)  # Wait for the new windows to open

# Step 5: Get all window handles
all_windows = driver.window_handles
print(f"All window handles: {all_windows}")

# Step 6: Switch to the second window (first child)
for window in all_windows:
    if window != main_window:  # Exclude the main window
        driver.switch_to.window(window)  # Switch to the child window
        # driver.find_element(By.ID, "accept").click()
        # alert = driver.switch_to.alert
        # alert.accept()
        # time.sleep(2)
        print(f"Switched to window: {window}")
        print(f"Window Title: {driver.title}")
        print(f"Window URL: {driver.current_url}")

        # Perform some action in the child window
        if "Google" in driver.title:  # Example: Check if it's the Google page
            search_box = driver.find_element(By.NAME, "q")
            time.sleep(2)
            search_box.send_keys("Selenium WebDriver")
            time.sleep(2)  # Wait to see the action

        # Close the child window (optional)
        driver.close()
        print(f"Closed window: {window}")

# Step 7: Switch back to the main window
driver.switch_to.window(main_window)
print(f"Back to main window: {driver.title}")

# Step 8: Close the browser
driver.quit()
