# import sys
# sys.path.insert(0,'/usr/lib/chromedriver')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()
import os
import time
from urllib.parse import urlparse
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_extension("ext.crx")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--window-size=100,80")
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome('chromedriver',options=chrome_options)

def logIN(user):
  #get method to Login
  driver.get("https://gridplays.com/login")
  phone = ["1718099973","1966788210","1839731938","1521459913","1632740232","1705063325","1708526085","1788889498","1928343865","1536261279","1935479804","1840084926","1878675968"]
  password = ["NKaX@Tw2E4r6YfnW&q","sw*RfWM87d!iMd#xa5","d7iX%KhRLnUkcLsiq4","bb42$6hGDZeEQP44#C","E9u5LN*fPAhe&R#peB","GgCx3rcQj77&g53^Bo","7$&DUv!*Moi!Dq^d74","Xgk&beZn@Mx6j6$y3x","sh5KPg6@tTUrrGv&vS","5Pb64eNK3oi%^8mfy6","RU9gM*8GBn9caWhDsU","jd!9CN%wigauD5&!tC","6t$f$NT#EUU6md&5xz"] 
  #wait = WebDriverWait(driver, 30) 
  driver.find_element(By.XPATH,'//input[@name="phone[]"]').send_keys(phone[user])
  driver.find_element(By.NAME,"pass").send_keys(password[user])
  # identifying the link with the help of link text locator
  driver.find_element(By.NAME,"login").click()
  driver.get('https://gridplays.com/qute/profile/index/src/profile')
  print("\nPhone No. : 0{} and ID: {}   [LOGGED IN]".format(phone[user],user))

#backp
def getToken():
    elements=driver.find_elements(By.TAG_NAME,'a')
    for i in elements:
        url=i.get_attribute("href")
        item_query=urlparse(url).query
        if len(item_query)>0:
            token = item_query
    return token
def battle(executionNO):
  try:
      driver.get('https://gridplays.com/qute/arena/')
      #battle using ticket
      driver.get('https://gridplays.com/qute/arena/index/act/ticket/id/420/src/battle')
      driver.find_element(By.LINK_TEXT,"Next round").click()
      skill_exe=1
      itn=0
      start_t=time.perf_counter()
      while True:
          try:
              myValue_ = driver.find_elements(By.XPATH,'/html/body/table/tbody/tr[8]/td[1]')[0]
              hp_my_=int(myValue_.text.split("/")[0])
          except:
              myValue_ = driver.find_elements(By.XPATH,'/html/body/table/tbody/tr[9]/td[1]')[0]
              hp_my_=int(myValue_.text.split("/")[0])
          try:
              driver.get("https://gridplays.com/qute/battle/index/src/arena")
              oponent_piyo = driver.find_element(By.XPATH,"/html/body/table/tbody/tr[3]/td[2]").text
              turn_no = driver.find_element(By.XPATH,"/html/body/table/tbody/tr[2]/td").text
              if hp_my_<600:
                  driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/div/a/img").click()
              else:
                  if oponent_piyo == "Earth Porcupine" or oponent_piyo == "Water Porcupine" or oponent_piyo == "Wind Ghost" or oponent_piyo == "Fire Drake":
                      if skill_exe==1:
                          driver.get("https://gridplays.com/qute/battle/index/act/skill/id/7?{}".format(getToken()))
                          skill_exe=0
                      else:
                          driver.get("https://gridplays.com/qute/battle/index/act/skill/id/1?{}".format(getToken()))
                  else:
                    # try:
                    if skill_exe==1:
                        skill_exe=0
                        try:
                            driver.get("https://gridplays.com/qute/battle/index/act/skill/id/21?{}".format(getToken()))
                        except:
                            driver.get("https://gridplays.com/qute/battle/index/act/skill/id/8?{}".format(getToken()))
                    else:
                        try:
                            driver.get("https://gridplays.com/qute/battle/index/act/skill/id/1?{}".format(getToken()))
                        except:
                            driver.get("https://gridplays.com/qute/battle/index/act/skill/id/8?{}".format(getToken()))

                    # except:
                        # driver.get("https://gridplays.com/qute/battle/index/act/skill/id/1?{}".format(getToken()))
          except:
              continue
          opValue_ = driver.find_elements(By.XPATH,'/html/body/table/tbody/tr[7]/td[2]')[0]
          hp_OP_=int(opValue_.text.split("/")[0])
          if hp_OP_ == 0:
              driver.find_element(By.LINK_TEXT,"Next").click()
              coolFind =driver.find_elements(By.TAG_NAME,'img')
              conText = driver.find_elements(By.XPATH,'/html/body/div[4]')[0].text
              allImages=[]
              coolFindStatus = 0
              for items in coolFind:
                  allImages.append(items.get_attribute('src'))
              coolURL = 'https://gridplays.com/qute/images/cool.gif'
              if coolURL in allImages or conText == 'You want to...\nAccept offering and quit fighting':
                  driver.find_element(By.LINK_TEXT,"Accept offering and quit fighting").click()
                  skill_exe=1
                  itn+=1
                  end_t=time.perf_counter()
                  exe_t=round((end_t-start_t),3)
                  print("Attempt No.:  {}  || Execution took: {}s".format(itn,exe_t))
                  start_t=time.perf_counter()
                  if itn ==executionNO:
                      condtn = False
                      driver.get("https://gridplays.com/logout")
                      print("Logout Successfull")
                      driver.close()
                      display.close()
                      break
                  driver.get('https://gridplays.com/qute/arena/index/act/ticket/id/420/src/battle')
                  driver.find_element(By.LINK_TEXT,"Next round").click()
                  continue
              else:
                  driver.find_element(By.LINK_TEXT,"Decline offering and continue fighting").click()
                  skill_exe=1
              driver.find_element(By.LINK_TEXT,"Next round").click()
          else:
              driver.find_element(By.LINK_TEXT,"Next").click()
  except:
      driver.get("https://gridplays.com/logout")
      print("Runtime Error")
      driver.close()
      display.close()
userNo=int(input("Enter User No: "))
logIN(userNo)
batNo=int(input("Enter Battle Count: "))
battle(batNo)
