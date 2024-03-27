from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
import requests
import os
import shutil

driver = webdriver.Chrome(executable_path="C:\\Users\\Zwanzig's PC\\Downloads\\chromedriver_win32\\0.00.exe")  # Adjust according to your browser "https://www.reddit.com/r/funnyvideos/" driver = webdriver.Chrome(ChromeDriverManager().install())

def download_file(url, local_filename,folder):
    """
    download file from url then saves it to given folder
    """
    safe_filename = re.sub(r'[\\/*?:"<>|]', '_', local_filename)
    safe_filename = folder+"\\"+safe_filename+".mp4"
    print(safe_filename)
    # Ensure the directory exists
    if not os.path.exists(os.path.dirname(safe_filename)):
        os.makedirs(os.path.dirname(safe_filename))
    
    # Proceed with downloading the file
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(safe_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)

def reset_videos():
    """
     Deletes and recreates the 'videos' directory to start fresh.
    """
    # Folder path
    folder_path = 'videos'

    # Check if the folder exists
    if os.path.exists(folder_path):
        # Remove the folder and all its contents
        shutil.rmtree(folder_path)
        print(f"The folder '{folder_path}' has been deleted.")

    # Create the new folder
    os.makedirs(folder_path)
    print(f"The folder '{folder_path}' has been created.")

def video_reddit(url_reddit):
    """
    Scrapes video URLs from a given Reddit page URL using Selenium.
    Returns a list of videos URLS and their title
    """
    # Initialize the WebDriver
    driver.get(url_reddit)

    # Scroll down gradually for 10 seconds
    start_time = time.time()
    while time.time() - start_time < 20:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Sleep briefly between scrolls

    #find mother html then take text then find source link
    text = driver.find_elements(By.CSS_SELECTOR, "article.w-full.m-0")

    # Find all <source> elements with a 'src' attribute
    source_elements = driver.find_elements(By.CSS_SELECTOR, "shreddit-player[src]")
    list_url = []
    # Iterate through the found <source> elements
    for url in source_elements:
        try:
            # Attempt to extract the 'src' attribute from each <source> element
            video_url = url.get_attribute('src')
            list_url.append([video_url])
        except Exception as e:
            print("Error processing element:", str(e))
            break  # Break the loop if an error occurs
    text = driver.find_elements(By.CSS_SELECTOR, "article.w-full.m-0")
    # Loop through each link and extract the aria-label attribute
    for i,element in enumerate(text):
        try:
            aria_label = element.get_attribute("aria-label")
            list_url[i].append(aria_label)
        except:
            break
    print(len(list_url))
    print(list_url[0])

    # Character that leads to removal of the string
    char_to_remove = 'https://v.redd.it'

    # Create a new list without strings that contain the character to remove
    filtered_list = [s for s in list_url if char_to_remove not in s[0] and len(s) != 1]
    print(filtered_list)
    for element in filtered_list:
        safe_filename = re.sub(r'[\\/*?:"<>|]', '_', element[1])
        element.append(safe_filename)

    # Clean up
    driver.quit()
    return filtered_list


def clean_up_folder(directory_path,final_list):
    """
    Cleans up a directory by removing currupt files 
    """
    # Specify the directory path  = 'C:\\Users\\zwanz\\Project Python\\Short_form_conten\\videos'
    # Loop through each file in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)  # Get the full path of the file
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Get the size of the file in bytes
            file_size = os.path.getsize(file_path)
            
            # If the file size is less than 100KB (100 * 1024 bytes)
            if file_size < 100 * 1024:
                os.remove(file_path)  # Delete the file
                final_list = [s for s in final_list if re.sub(r'[\\/*?:"<>|]', '_', s) not in filename]
    return final_list



