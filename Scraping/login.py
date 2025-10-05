import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd 



#Step 1 : to launch the browser
driver = webdriver.Chrome()


#step2: to control the elements  and the nevigate  the  browser
driver.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=774088017322&hvpos=&hvnetw=g&hvrand=10276592793388103867&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061919&hvtargid=kwd-64107830&hydadcr=14452_2429115&gad_source=1")
driver.maximize_window()
time.sleep(2)


#step 4 : to interaction to sign up
sign_btn = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='nav-link-accountList']/a"))
    )
sign_btn.click()
print("sign button clicked successfully")

   
#step 5: fill the empty field
driver.find_element(By.ID,"ap_email_login").send_keys("Enter your number")

ctn_btn = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CLASS_NAME,"a-button-input"))
    )
ctn_btn.click()
print("Continue button clicked successfully")

driver.find_element(By.ID,"ap_password").send_keys("Test@123")

#step 6: to create the account
create_btn = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,"signInSubmit"))
)

create_btn.click()
print("To sign in successfully")
time.sleep(5)


today_deal = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.LINK_TEXT,"Bestsellers"))
)


today_deal.click()
print("To click the deal's succesfully")
time.sleep(3)

# EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Mobiles']"))

see = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div/a"))
)
see.click()

time.sleep(3)
print("successful to click")





products = driver.find_elements(By.CLASS_NAME,"_cDEzb_p13n-sc-css-line-clamp-3_g3dy1")
prices = driver.find_elements(By.CLASS_NAME,"_cDEzb_p13n-sc-price_3mJ9Z")
# rates = driver.find_elements(By.CLASS_NAME,"a-icon-alt")
# peoples = driver.find_elements(By.CLASS_NAME,"a-size-small")


data = []

for p,pri in zip(products,prices):
    data.append({"Product": p.text,"Prices": pri.text})  


df = pd.DataFrame(data)
df.to_csv("amazon1.csv")
