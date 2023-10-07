import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    def test_basic_authentication(self):
        driver = self.driver
        username = "admin"
        password = "admin"
        url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
        driver.get(url)
        self.wait_for_page_to_load()
        self.assertIn("Congratulations!", driver.page_source)

    def test_checkboxes(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        self.wait_for_page_to_load()
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        self.assertFalse(checkboxes[0].is_selected())
        self.assertTrue(checkboxes[1].is_selected())
        checkboxes[0].click()
        checkboxes[1].click()
        self.assertTrue(checkboxes[0].is_selected())
        self.assertFalse(checkboxes[1].is_selected())

    def test_dynamic_controls(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/dynamic_controls")
        self.wait_for_page_to_load()

        enable_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Enable')]")
        input_field = driver.find_element(By.CSS_SELECTOR, "input[type='text'][disabled][style='width: 30%;']")
        self.assertFalse(input_field.is_enabled())

        enable_button.click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']:not([disabled])[style='width: 30%;']")))
        input_field = driver.find_element(By.CSS_SELECTOR, "input[type='text']:not([disabled])[style='width: 30%;']")
        self.assertTrue(input_field.is_enabled())

    def test_dropdown(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/dropdown")
        self.wait_for_page_to_load()

        dropdown = driver.find_element(By.ID, "dropdown")
        webdriver.support.ui.Select(dropdown).select_by_visible_text("Option 1")

        selected_option = webdriver.support.ui.Select(dropdown).first_selected_option
        self.assertEqual(selected_option.text, "Option 1")

    def test_hover(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/hovers")
        self.wait_for_page_to_load()

        avatars = driver.find_elements(By.CLASS_NAME, "figure")
        for avatar in avatars:
            webdriver.ActionChains(driver).move_to_element(avatar).perform()
            user_name = avatar.find_element(By.TAG_NAME, "h5")
            self.assertTrue(user_name.is_displayed())

    def test_key_presses(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/key_presses")
        self.wait_for_page_to_load()

        input_field = driver.find_element(By.ID, "target")
        input_field.send_keys(Keys.SHIFT)
        result = driver.find_element(By.ID, "result")
        self.assertEqual(result.text, "You entered: SHIFT")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
