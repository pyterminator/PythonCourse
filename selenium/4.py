import time 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

first_video_x_path = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-item-renderer[104]"

driver.get("https://youtube.com/@pyterminator/videos")

while True:
    driver.execute_script("window.scrollTo(0, 100000)")

    try:
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
            (By.XPATH, first_video_x_path)
        ))
        first_video = driver.find_element(By.XPATH, first_video_x_path)
        break
    except:
        continue


with open("videos.csv", "a+", encoding="utf-8") as file:
        
    for number in range(1, 106):
        try:
            x_path = f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-item-renderer[{number}]/div/ytd-rich-grid-media/div[1]/div[3]/div[2]/h3/a/yt-formatted-string'
            x_path_for_view = f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-item-renderer[{number}]/div/ytd-rich-grid-media/div[1]/div[3]/div[2]/ytd-video-meta-block/div[1]/div[2]/span[1]'
            
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, x_path)))
            video_name = driver.find_element(By.XPATH, x_path)
            video_view = driver.find_element(By.XPATH, x_path_for_view)

            file.write(f"{video_name.text}|||{video_view.text}\n")


        except:
            continue

driver.quit()