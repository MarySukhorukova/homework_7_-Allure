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
@allure.story('Шаги с декоратором @allure.step')
@allure.link('https://github.com', name='Testing')
def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    open_repository("eroshenkoam/allure-example")
    open_issues_tab()
    should_see_issue_number("#76")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Открываем репозиторий {repo}")
def open_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issues_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие issue с номером {number}")
def should_see_issue_number(number):
    s(by.partial_text(number)).should(be.visible)