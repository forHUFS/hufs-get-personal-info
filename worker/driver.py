from selenium                          import webdriver
from selenium.webdriver.chrome.options import Options


class WebDriver(webdriver.Chrome):
    def __init__(self):
        path    = '/Users/0417taehyun/Documents/Project/HUFSpace/WEB/hufs-get-personal-info/chromedriver'
        options = Options()


        webdriver.Chrome.__init__(
            self,
            executable_path = path,
            options         = options
        )
    