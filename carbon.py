import os, time
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver

SCHEME = "https"
DOMAIN = "carbon.now.sh"

def carbon(code, lang="auto"):
    config = {
        "pv": "10px",
        "ph": "10px",
        "t": "vscode",
        "wa": "false",
        "l": lang,
        "code": code
    }

    parameters = '&'.join([f"{key}={urllib.parse.quote_plus(value)}" for key, value in config.items()])

    url = f"{SCHEME}://{DOMAIN}/?{parameters}"

    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.folderList', 2)  # custom location
    profile.set_preference('browser.download.manager.showWhenStarting', False)
    profile.set_preference('browser.download.dir', os.getcwd())
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'image/png')
    # profile.set_preference('extensions.logging.enabled', True)
    
    options = webdriver.FirefoxOptions()
    options.add_argument("--safe-mode")


    os.environ['MOZ_HEADLESS'] = '1'
    browser = webdriver.Firefox(profile, options=options)
    

    browser.get(url)
    browser.find_element_by_xpath("//*[contains(text(), 'Export')]").click()
    browser.find_element_by_id("export-png").click()

    time.sleep(1)

code = """package main

import "fmt"

func main() {
    fmt.Println("hello world")
}

"""

carbon(code)


