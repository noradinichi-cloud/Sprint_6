from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка принятия кук
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    # Логотипы в шапке
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")

    # Кнопки "Заказать" (верхняя в шапке и нижняя в разделе "Как это работает")
    ORDER_BUTTON_TOP = (By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']")

    # Раздел "Вопросы о важном" (шаблоны локаторов для подстановки номера вопроса от 0 до 7)
    FAQ_QUESTION = (By.ID, "accordion__heading-{}")
    FAQ_ANSWER = (By.ID, "accordion__panel-{}")
