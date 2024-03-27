from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import re
import random




def click_element_XPATH(XPATH,driver):
    """
    clicks on an element using XPATH
    """
    try:
        best_sellers_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, XPATH))
        )
        best_sellers_link.click()
        return best_sellers_link
    except Exception as e:
        print("Error: ", e)
    return False


def login(list_credentials,driver):
    """
    Login into instargram using provided credentials
    """

    # Assuming 'driver' is your WebDriver instance
    wait = WebDriverWait(driver, 10) # Waits for up to 10 seconds before throwing a TimeoutException unless it finds the element

    decline_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Decline optional cookies')]")))

    # Click the button
    decline_button.click()
    sleep(3)
    # Replace 'textBoxId' with the actual ID of the text box
    text_box = wait.until(EC.presence_of_element_located((By.XPATH,
                '//*[@id="loginForm"]/div/div[1]/div/label/input')))

    # Now send keys
    text_box.send_keys(list_credentials[0])

    wait = WebDriverWait(driver, 10) # Waits for up to 10 seconds before throwing a TimeoutException unless it finds the element

    # Replace 'textBoxId' with the actual ID of the text box
    text_box = wait.until(EC.presence_of_element_located((By.XPATH,
                '//*[@id="loginForm"]/div/div[2]/div/label/input')))

    # Now send keys
    text_box.send_keys(list_credentials[1])
    click_element_XPATH("//*[@id=\"loginForm\"]/div/div[3]/button",driver)

def upload_video_insta(filename,caption,driver,filepath):
    """
    uploads the video onto instagram 
    """
    sleep(10)
    text = ['funnymemes', 'funnyreels', 'memestagram', 'comedyreels', 'mdr', 'lmao',
         'humour',  'viral', 'trendingreels', 'viralvideos', 'lol', 'fun', 'dankmemes ', 'funnyvideos',
          'memes',  'comedy', 'funnyjokes', 'viralpost', 'comedyvideos',
           'funnymemesdaily', 'viralmemes']
    caption += "\n #"+text.pop(random.randint(0,len(text))-1)+" #"+text.pop(random.randint(0,len(text))-1)
    +" #"+text.pop(random.randint(0,len(text))-1)+" #"+text.pop(random.randint(0,len(text))-1)
    +" #"+text.pop(random.randint(0,len(text))-1)+" #"+text.pop(random.randint(0,len(text))-1)
    +" #"+text.pop(random.randint(0,len(text))-1)+" #"+text.pop(random.randint(0,len(text))-1)
    +" #"+text.pop(random.randint(0,len(text))-1)+" #"+text.pop(random.randint(0,len(text))-1)

    wait = WebDriverWait(driver, 10)
    create_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Create']")))
    create_button.click()
    # Specify the path to the file you want to upload
    file_path = filepath + "{}.mp4".format(filename)
    sleep(2)
    # Locate the file input element and send the file path
    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']._ac69")
    file_input.send_keys(file_path)
    sleep(10)
    wait = WebDriverWait(driver, 10)
    # Wait for the button to be clickable
    #change fromat
    click_element_XPATH("/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div[4]/button",driver)
    sleep(2)
    click_element_XPATH("/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button",driver)
    sleep(2)
    click_element_XPATH("/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div[1]/div/div[1]/span",driver)
    sleep(2)
    click_element_XPATH("/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div",driver)
    sleep(2)
    click_element_XPATH("/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div",driver)
    sleep(2)
    caption_text = wait.until(EC.presence_of_element_located((By.XPATH,
                    "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div[1]"))).send_keys(caption)
    post_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div")))

    # Click the button
    post_button.click()
    sleep(30)
    click_element_XPATH("/html/body/div[6]/div[1]/div/div[2]/div",driver)



def post_on_insta(caption,list_credentials):
    """
    Combination of all previous function to post all to instagram
    """
    #driver = webdriver.Chrome()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Set up the driver
    sleep(1)
    # Your remaining Selenium code
    driver.maximize_window()
    driver.get("https://www.instagram.com")  # Correct the URL if needed
    print(driver.title, driver.current_url)

    login(list_credentials,driver)

    sleep(30)

    #make a function upload_video_tiktok()
    upload_video_insta(re.sub(r'[\\/*?:"<>|]', '_', caption),caption,driver)
    sleep(20)

    driver.quit()
    print("end")

