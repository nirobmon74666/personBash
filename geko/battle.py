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
    
profile= webdriver.FirefoxProfile(proPath)
profile.add_extension(extension='ub.xpi')
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()

driver = webdriver.Firefox(firefox_profile=profile)
driver.get("https://gridplays.com/")
time.sleep(10)

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
                  if oponent_piyo == "Alien Piyo":
                      try:
                          driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[1]/div/a[1]/img").click()
                      except:
                          driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[1]/div/a[3]/img").click()

                  elif oponent_piyo == "Earth Porcupine" or oponent_piyo == "Water Porcupine":
                      if skill_exe==1:
                          driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[1]/div/a[2]/img").click()
                          skill_exe=0
                      else:
                          driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[1]/div/a[3]/img").click()

                  elif oponent_piyo == "Big Onion" or oponent_piyo == "Pink Onion" or oponent_piyo == "Wood Trunk" or oponent_piyo == "Daisy Naga":
                      if skill_exe==1:
                          driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[1]/div/a[4]/img").click()
                          skill_exe=0
                      else:
                          driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[1]/div/a[3]/img").click()

                  elif oponent_piyo == "Stone Pig" or oponent_piyo == "Green Pig":
                      if skill_exe==1:
                          driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[1]/div/a[2]/img").click()
                          skill_exe=0
                      else:
                          driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[1]/div/a[3]/img").click()

                  elif  oponent_piyo == "Rockie" or oponent_piyo == "Ameoba" or oponent_piyo == "Killer Machine" or oponent_piyo == "Earth Naga" or oponent_piyo == "Bat" or oponent_piyo == "Mad Squirrel":
                      if skill_exe==1:
                          driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[1]/div/a[1]/img").click()
                          skill_exe=0
                      else:
                          driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[1]/div/a[3]/img").click()
                  else:
                      driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[1]/div/a[3]/img").click()

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
                      display.stop()
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
      display.stop()
userNo=int(input("Enter User No: "))
logIN(userNo)
batNo=int(input("Enter Battle Count: "))
battle(batNo)
