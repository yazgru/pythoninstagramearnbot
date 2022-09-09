from ast import Try
from logging import exception
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
chrome_options = Options()
options.add_argument("user-data-dir=C:\\Users\\yazilimgrup\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
driver=webdriver.Chrome(executable_path=r'C:\Users\yazilimgrup\Desktop\webscrap\chromedriver.exe',chrome_options=options)
chrome_options.add_experimental_option("detach", True) #prevent window from closing

driver.get("https://greatonlinetools.com/autoliker/")

sleep(2)
e = driver.find_element(By.CSS_SELECTOR,"#searchbtn")
# username=driver.find_element(By.CSS_SELECTOR,"#username")
# username.send_keys("yazilimgrup")
sleep(2)
e.click()
tekrar = 0
sleep(20)
while tekrar < 100:
    tekrar +=1
    sleep(3)
    driver.get("https://greatonlinetools.com/ig-autoliker/earn/")
    sleep(5)
    takip=driver.find_element(By.CSS_SELECTOR,"#actionbtn")
    if takip.text=="FOLLOW":
        sleep(4)
        takip.click()
        sleep(5)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        sleep(5)
        takippp=driver.find_element(By.XPATH,"//*[contains(text(),'Takip Et')]")
        takippp.click()
        sleep(8)
        driver.close()
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)
    sleep(5)
    driver.get("https://greatonlinetools.com/ig-autoliker/earn/")

    sleep(5)
    begen=driver.find_element(By.CSS_SELECTOR,"#actionbtn")
    sleep(2)
    if begen.text=="LIKE":
        sleep(4)
        begen.click()
        print('Beğen tıklandı')
        sleep(5)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        sleep(5)
        begenn=driver.find_element(By.CLASS_NAME,'_aamw')
        begenn.click()
        sleep(8)
        driver.close()
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)
    sleep(5)
    driver.get("https://greatonlinetools.com/ig-autoliker/earn/")
  

    
#searchaa=driver.find_element(By.XPATH,'//input[@placeholder="Ara"]')
#searchaa.send_keys('teknoloji')

   
    

