from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
# from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 600))
# display.start()
import os
import time
from urllib.parse import urlparse

with open('path.txt') as f:
    proPath = f.read()
truePath=proPath[:len(proPath)-1]
    
profile= webdriver.FirefoxProfile(truePath)
profile.add_extension(extension="{}/extensions/uBlock0@raymondhill.net.xpi".format(truePath))
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()

driver = webdriver.Firefox(firefox_profile=profile)
driver.set_window_size(100,80)
driver.get("https://gridplays.com/")
time.sleep(10)

def logIn(user):
    #get method to Login
    driver.get("https://gridplays.com/login")
    #to refresh the browser
    phone = ["1718099973","1966788210","1839731938","1521459913","1632740232","1705063325","1708526085","1788889498","1928343865","1536261279","1935479804","1840084926","1878675968"]
    password = ["NKaX@Tw2E4r6YfnW&q","sw*RfWM87d!iMd#xa5","d7iX%KhRLnUkcLsiq4","bb42$6hGDZeEQP44#C","E9u5LN*fPAhe&R#peB","GgCx3rcQj77&g53^Bo","7$&DUv!*Moi!Dq^d74","Xgk&beZn@Mx6j6$y3x","sh5KPg6@tTUrrGv&vS","5Pb64eNK3oi%^8mfy6","RU9gM*8GBn9caWhDsU","jd!9CN%wigauD5&!tC","6t$f$NT#EUU6md&5xz"]
    #wait = WebDriverWait(driver, 30) 
    driver.find_element(By.XPATH,'//input[@name="phone[]"]').send_keys(phone[user])
    driver.find_element(By.NAME,"pass").send_keys(password[user])
    # identifying the link with the help of link text locator
    driver.find_element(By.NAME,"login").click()
    driver.get('https://gridplays.com/qute/profile/index/src/profile')
    print("\nPhone No. : 0{} and ID: {}".format(phone[user],user))
    print(driver.find_element(By.XPATH,'/html/body/div[6]').text)

# trophy sending
def getToken():
    elements=driver.find_elements(By.TAG_NAME,'a')
    for i in elements:
        url=i.get_attribute("href")
        item_query=urlparse(url).query
        if len(item_query)>0:
            token = item_query
    return token


logIn(0)
driver.get("https://gridplays.com/qute/trophy/index/act/select/src/board")
for i in range(0, 1000):
    s_url= "https://gridplays.com/qute/trophy/index/act/select/id/236/subpage/0/src/board?{}".format(getToken())
    print(s_url)
    driver.get(s_url)
    time.sleep(59)
driver.get("https://gridplays.com/logout")
driver.close()
