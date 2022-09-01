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
    phone=['1310438454','1750538161', '1817846118', '1858342872', '1815551971', '1581292523', '1775753972', '1858342850', '1740120563', '1626690700', '1928410081', '1764269319', '1935052275', '1852461441', '1925102490', '1851759760', '1300163738', '1301980223', '1748376601', '1630480904', '1977454725', '1735325058', '1792485654', '1581292819', '1768008066', '1752615130','1799409077', '1612700824', '1321744725', '1608214887', '1751695920', '1842424680', '1884365092', '1740569341', '1817552130','1797481703', '1320420275', '1765158679', '1320420274', '1908815923', '1734658457', '1719456413', '1755331044', '1790916862', '1521108344', '1754428279', '1870536709']
    password=['Anupama Das','anupama_jui1', 'anupama_jui2', 'anupama_jui3', 'anupama_jui4', 'jikrullah2', 'jikrullah1', 'jikrullah3', 'jikrullah5', 'jikrullah5', 'juiful1', 'juiful11', 'juipagli', 'jikrullah77', 'juiful13', 'anupagli', 'valoaci', 'juipagli3', 'janina12', 'foring', 'anupama', 'alalala', 'foundation', 'fokinni', 'testtest', 'fulersubas','kheyeco', 'kijani', 'tarenare', 'asonakn', '232323', 'eieieiei', 'arenare', 'janina', 'janina','1234567', '123456789', '012345', '0123456', 'shayakh al abid 2', 'tapan das', 'shayakh al abid', '123456', 'shoikot mahmud', 'nirupama mou', 'nirupama das', '01955026116Aa+']
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
    mineAll()
#     memoryAll()
   # slotmachine()
    #feednPlay()
    reFillyo()
    logOUT()
driver.close()
display.stop()
