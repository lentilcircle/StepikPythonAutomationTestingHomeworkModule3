import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        help="Язык браузера в тестах (пример: --language=ru)"
    )

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")

    if not language:
        raise pytest.UsageError("Необходимо указать --language (пример: --language=ru)")
    
    print(f"\nВыбран язык: {language}")
    options = Options()
    options.add_experimental_option("prefs",
            {f"intl.accept_languages": language})
    
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # чтоб убрать "мусорные" сообщения DevTools и GCM

    options.add_argument("--log-level=3")
    # убрать "мусорные" логи хрома (оставить только сообщения о критических ошибках)

    try:
        browser = webdriver.Chrome(options=options)
    except Exception as e:
        raise RuntimeError(f"Не удалось запустить Chrome: {e}")
    
    yield browser
    browser.quit()


