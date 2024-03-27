
#https://www.google.com/travel/flights?q=Flights%20to%20IST%20from%20BLQ%20on%202024-10-24%20oneaway                  - gidiş
#https://www.google.com/travel/flights?q=Flights%20to%20IST%20from%20BLQ%20on%202024-10-24%20through%202024-10-30     - gidiş-dönüş


from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

dosya = "uçuş_bilgileri.txt"

with open(dosya, "w",encoding="utf-8") as dosya1:
        
    url_havalimanı = f"https://www.google.com/travel/flights?q=Flights%20from%20IST%20to%20BLQ%20on%202024-10-24%20oneway"
    driver.get(url_havalimanı)

    time.sleep(5)

    flight_elements = driver.find_elements(By.XPATH, '//body[@id = "yDmH0d"]//div[@jsname="qJTHM"]//li[@class="pIav2d"]')

    uçuşlar = []
    for flight_element in flight_elements:
        uçuşlar.append(flight_element.text.replace("\n", " "))

    dosya1.write(f"Tarih:24.10.2024\n")
    for uçuş in uçuşlar:
        dosya1.write(uçuş + "\n")
driver.quit()
