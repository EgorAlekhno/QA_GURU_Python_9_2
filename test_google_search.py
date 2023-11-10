import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def setup_browser():
    browser.config.window_width = 1440
    browser.config.window_height = 900
    browser.open('https://google.com')

def test_google_should_find_selene_with_pytest(setup_browser):
   browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
   browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
   browser.quit()
    
def test_google_should_not_find_selene_with_pytest(setup_browser):
   browser.element('[name="q"]').should(be.blank).type('wtvwtvbwtrbrttbrwasvasfvasfvdafv').press_enter()
   browser.element('[class="card-section"]').should(have.text('По запросу wtvwtvbwtrbrttbrwasvasfvasfvdafv ничего не найдено.'))
