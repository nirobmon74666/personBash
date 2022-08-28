# import sys
# sys.path.insert(0,'/usr/lib/chromedriver')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from urllib.parse import urlparse
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_extension("ext.crx")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome('chromedriver',options=chrome_options)
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

#Logout & Close Driver
def logOUT():
    driver.get("https://gridplays.com/logout")

#Refill YO
def reFillyo():
    try:
        driver.get("https://gridplays.com/qute/wallet/index/src/profile")
        driver.get('https://gridplays.com/qute/wallet/index/id/1/src/profile')
        driver.find_element(By.LINK_TEXT,"Claim").click()
        print("Refill Success")
    except:
        print("Refill Failed")
        logOUT()

def feedO():
    #Feed
    driver.get("https://gridplays.com/qute/creature/feed/id/17/subpage/0")
    driver.find_element(By.LINK_TEXT,"Feed").click()
    time.sleep(14)
    driver.get("https://gridplays.com/qute/creature/index/src/creature")

def playnSleep():
    #play and Sleep
    driver.get("https://gridplays.com/qute/creature/plern/id/11/subpage/0")
    driver.find_element(By.LINK_TEXT,"Play").click()
    time.sleep(14)
    driver.get("https://gridplays.com/qute/creature/index/src/creature")
    driver.get('https://gridplays.com/qute/creature/index/src/profile')
    driver.find_element(By.LINK_TEXT,'bed').click()

def feednPlay():
    #Play and Feed
    driver.get("https://gridplays.com/qute/creature/plern/id/401/subpage/0")
    driver.find_element(By.LINK_TEXT,"Play").click()
    driver.get("https://gridplays.com/qute/creature/feed/id/192/subpage/0")
    driver.find_element(By.LINK_TEXT,"Feed").click()
    time.sleep(11)
    driver.get("https://gridplays.com/qute/creature/index/src/creature")

#Collecting Harvest
def collectHV():
    try:
        driver.get("https://gridplays.com/qute/creature/index/src/profile")
        hv = 0
        while hv<3:
            if driver.find_element(By.LINK_TEXT,"Open").text == "Open":
                driver.find_element(By.LINK_TEXT,"Open").click()
                driver.find_element(By.LINK_TEXT,"Close").click()
            hv=hv+1
    except:
        #place item
        hv=0
        try:
            while hv<2:
                driver.get("https://gridplays.com/qute/creature/plant/id/96/slot/{}/subpage/0".format(hv))
                driver.find_element(By.LINK_TEXT,"Place item").click()
                hv=hv+1
            print("Placing Success")
            #time.sleep(4)
            driver.get("https://gridplays.com/qute/creature/index/src/creature")
        except:
            print("Placing Failed")

#Placing Items
def placingItem():
    while hv<2:
        driver.get("https://gridplays.com/qute/creature/plant/id/96/slot/{}/subpage/0".format(hv))
        driver.find_element(By.LINK_TEXT,"Place item").click()
        hv=hv+1


#Slotmachine
def slotmachine():
    try:
        driver.get('https://gridplays.com/qute/slot/index/src/creature')
        bull = True
        while bull:
            driver.find_element(By.LINK_TEXT,"Spin").click()
    except:
        print("Slotmachine Completed")

def mineDigging():
    driver.get('https://gridplays.com/qute/job')
    try:
        if  driver.find_element(By.XPATH,"/html/body/div[16]/table/tbody/tr/td[2]/div/a[2]").text == 'Start Job' or driver.find_element_by_xpath("/html/body/div[16]/table/tbody/tr/td[2]/div/a[1]").text == "Continue Job":
            driver.find_element(By.LINK_TEXT,"/html/body/div[16]/table/tbody/tr/td[2]/div/a[1]").click()
    except:
            driver.find_element(By.XPATH,"/html/body/div[16]/table/tbody/tr/td[2]/div/a[2]").click()
    driver.refresh()
    driver.refresh()
    driver.refresh()
    driver.refresh()
    driver.refresh()
    driver.refresh()
    while True:
        true_image=[]
        page = ['https://gridplays.com/qute/missing/index/show/0','https://gridplays.com/qute/missing/index/show/1','https://gridplays.com/qute/missing/index/show/2']
        for page_no in page:
            driver.get(page_no)
            j = 1
            bottom_image=[]
            _xpath_bottom_S=[]
            while j < 5:
                _xpath_bottom="/html/body/div[8]/a[{}]/img".format(j)
                _xpath_bottom_S.append(_xpath_bottom)
                crystal=driver.find_element(By.XPATH,_xpath_bottom)
                src_url=crystal.get_attribute("src")
                bottom_image.append(os.path.splitext(os.path.basename(urlparse(src_url).path))[0])
                j=j+1

            top_image=[]
            k=1
            _xpath_top_S=[]
            while k<10:
                _xpath_top= "/html/body/div[5]/div[2]/center/div/img[{}]".format(k)
                _xpath_top_S.append(_xpath_top)
                crystal_top=driver.find_element(By.XPATH,_xpath_top)
                src_url_top=crystal_top.get_attribute("src")
                top_image.append(os.path.splitext(os.path.basename(urlparse(src_url_top).path))[0].split("_")[0])    
                k=k+1
            i=0
            for b_i in bottom_image:
                for t_i in top_image:
                    if b_i == t_i:
                        true_image.append(b_i)

        _index=bottom_image.index(list(set(bottom_image).difference(true_image))[0])
        #click
        _fxpath= _xpath_bottom_S[_index]
        crystal=driver.find_element(By.XPATH,_fxpath)
        crystal.click()
        it=driver.find_element(By.XPATH,"/html/body/div[6]/a").text
        if it == "Get Job's Reward":
            driver.find_element(By.LINK_TEXT,"Get Job's Reward").click()
            driver.find_element(By.LINK_TEXT,"Check another job").click()
            print("▣", end="")
            driver.find_element(By.XPATH,"/html/body/div[16]/table/tbody/tr/td[2]/div/a[2]").click()
            continue
        else:
            driver.find_element(By.LINK_TEXT,"Keep working").click()

def mineAll():
    try:
        driver.get('https://gridplays.com/qute/job')
        driver.find_element(By.LINK_TEXT,'Start Job').click()
        #driver.find_element(By.LINK_TEXT,'Ok').click()
        mineDigging()
    except:
        try:
            mineDigging()
        except:
            print("\nJob UNDONE")
    try:
        driver.get('https://gridplays.com/qute/job/index/src/creature')
        driver.find_element(By.LINK_TEXT,'Quit Job').click()
        driver.find_element(By.LINK_TEXT,'ok').click()
        print("Job Quit: Success")
    except:
        print("Job Quit: Failed")
    try:
        driver.get('https://gridplays.com/qute/creature/index/src/profile')
        driver.find_element(By.LINK_TEXT,'bed').click()
    except:
        print("Sleep: Failed")



def getToken():
    elements=driver.find_elements(By.TAG_NAME,'a')
    for i in elements:
        url=i.get_attribute("href")
        item_query=urlparse(url).query
        if len(item_query)>0:
            token = item_query
    return token

def getSrcPhrase(url):
    driver.get(url)
    all_images=driver.find_elements(By.TAG_NAME,"img")
    i=0
    figure_phrase=[]
    for i in all_images:
        src_ele=i.get_attribute("src")
        find_src=src_ele.split("/")
        if len(src_ele)>=50 and find_src[6]=="vision":
            figure_phrase.append(src_ele)
    return figure_phrase

def memoryGame():
    driver.get('https://gridplays.com/qute/job')
    try:
        if  driver.find_element(By.XPATH,"/html/body/div[13]/table/tbody/tr/td[2]/div/a[2]").text == 'Start Job' or driver.find_element_by_xpath("/html/body/div[13]/table/tbody/tr/td[2]/div/a[1]").text == "Continue Job":
            driver.find_element(By.LINK_TEXT,"/html/body/div[13]/table/tbody/tr/td[2]/div/a[1]").click()
    except:
            driver.find_element(By.XPATH,"/html/body/div[13]/table/tbody/tr/td[2]/div/a[2]").click()
    while True:
        j=1
        genuine_figure=getSrcPhrase("https://gridplays.com/qute/vision/index/show/0")
        while j<5:
            current_figure=getSrcPhrase("https://gridplays.com/qute/vision/index/show/{}".format(j))
            if current_figure==genuine_figure:
                final_url= "https://gridplays.com/qute/vision/index/act/ans/number/{}?{}".format(j-1,getToken())
                driver.get(final_url)
            j+=1
        
        it=driver.find_element(By.XPATH,"/html/body/div[8]/a").text
        if it == "Get Job's Reward":
            driver.find_element(By.LINK_TEXT,"Get Job's Reward").click()
            driver.find_element(By.LINK_TEXT,"Check another job").click()
            print("▣", end="")
            driver.refresh()
            driver.refresh()
            driver.refresh()
            driver.refresh()
            driver.refresh()
            driver.refresh()
            driver.find_element(By.XPATH,"/html/body/div[13]/table/tbody/tr/td[2]/div/a[2]").click()
            continue
        else:
            driver.find_element(By.LINK_TEXT,"Keep working").click()


def memoryAll():
    try:
        driver.get('https://gridplays.com/qute/job')
        driver.find_element(By.LINK_TEXT,'Start Job').click()
        # driver.find_element(By.LINK_TEXT,'Ok').click()
        memoryGame()
    except:
        try:
            memoryGame()
        except:
            print("\nJob UNDONE")
    try:
        driver.get('https://gridplays.com/qute/job/index/src/creature')
        driver.find_element(By.LINK_TEXT,'Quit Job').click()
        driver.find_element(By.LINK_TEXT,'ok').click()
        print("Job Quit: Success")
    except:
        print("Job Quit: Failed")
    try:
        driver.get('https://gridplays.com/qute/creature/index/src/profile')
        driver.find_element(By.LINK_TEXT,'bed').click()
    except:
        print("Sleep: Failed")

user=0
while user<13:
    logIn(user)
    if user==0:
        print ("Bypassed")
    else:
        collectHV()
        #mineAll()
    user+=1
    # mineAll()
    memoryAll()
   # slotmachine()
    #feednPlay()
    #reFillyo()
    logOUT()
driver.close()
display.stop()
