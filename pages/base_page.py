import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step("Кликнуть на элемент через JS")
    def click_with_js(self, locator, timeout=15):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст '{text}' в поле")
    def send_keys_to_input(self, locator, text, timeout=15):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=15):
        return self.wait_for_element(locator, timeout).text

    @allure.step("Проскроллить страницу до элемента")
    def scroll_to_element(self, locator, timeout=15):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Переключиться на новую вкладку браузера")
    def switch_to_new_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    @allure.step("Подождать, пока URL будет содержать '{expected_url}'")
    def wait_for_url_contains(self, expected_url, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(expected_url)
        )

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url
