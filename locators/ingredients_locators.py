from selenium.webdriver.common.by import By

class IngredientsLocators:
    # Флюоресцентная булка R2-D3 в конструкторе
    fluorescent_bun = (By.XPATH, '//img[@alt = "Флюоресцентная булка R2-D3"]')

    # Соус фирменный Space Sauce
    space_sauce = (By.XPATH, '//img[@alt = "Соус фирменный Space Sauce"]')

    # Счетчик у соуса фирменного Space Sauce
    space_sauce_counter = (By.XPATH, '//img[@alt = "Соус фирменный Space Sauce"]/parent::a/div/p[contains(@class, "counter_counter__num")]')

    # Начинка Говяжий метеорит (отбивная)
    filling_meat = (By.XPATH, '//img[@alt = "Говяжий метеорит (отбивная)"]')

    # Конструктор бургеров
    burger_constructor_basket = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')
