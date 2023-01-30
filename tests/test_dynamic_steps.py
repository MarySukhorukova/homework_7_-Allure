import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag('web')
@allure.label('owner', 'marysukhorukova')
@allure.severity(Severity.NORMAL)
@allure.feature('Проверка наличия задачи в репозитории')
@allure.story('Лямбда шаги через with allure.step')
@allure.link('https://github.com', name='Testing')
def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()

    with allure.step("Открываем репозиторий"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие issue с номером 76"):
        s(by.partial_text("#76")).should(be.visible)