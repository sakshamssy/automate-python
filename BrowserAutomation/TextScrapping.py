from selenium import webdriver

def get_driver():
    #Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars") #disable infobars on webpages
    options.add_argument("start-maximized")  #webpages remove info in minimised option
    options.add_argument("disable-dev-shm-usage") #avoid linux se scraping problems
    options.add_argument("no-sandbox") #for greater accessebility
    options.add_experimental_options("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://arcbphc.vercel.app/")
    return driver

def main():
    driver = get_driver()
    element = driver.find_element(by="xpath",value ="/html/body/div/div[2]/div[2]/span[2]")
    return element

print(main())