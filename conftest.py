import pytest
from selenium import webdriver

exec_path = r"E:\\Novito\\Webdrivers\\chromedriver_win32\\chromedriver.exe"
exec_path2 = r"E:\\Novito\\Webdrivers\\geckodriver-v0.27.0-win64\\geckodriver.exe"


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=exec_path)
        print("launching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=exec_path2)
        print("launching firefox browser")
    else:
        driver = webdriver.Chrome(executable_path=exec_path) #this is the default browser (paja poner el Ie)
    return driver


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the browser value
    return request.config.getoption("--browser")


# Pytest HTML reports

#A hook for adding environment info to a HTML report
def pytest_configure(config):

    config._metadata['Project Name'] = 'nopCommerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Novito'

#A hook for delete/modify environment info to a HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)