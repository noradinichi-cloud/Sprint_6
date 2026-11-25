from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Первый экран: "Для кого самокат"
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTION = (By.XPATH, "//div[@class='select-search__select']//button[contains(., '{}')]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Второй экран: "Про аренду"
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-menu']/div[text()='{}']")
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_SUBMIT_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")

    # Модальное окно подтверждения и успешного заказа
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(., 'Заказ оформлен')]")
