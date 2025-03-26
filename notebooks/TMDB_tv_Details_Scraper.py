from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import pandas as pd
import time 


# Set up headless Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (optional but recommended)
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems in containers

tvShow_data = []
if __name__ == "__main__":
    # driver  = webdriver.Chrome()

    df = pd.read_csv("Merged_TMDB_tvShow_URLs.csv") 
    # import pdb; pdb.set_trace()   
    tvShow_urls = df['Url'].to_list()

    for tvShow_url in tqdm(tvShow_urls):
        try:
            driver  = webdriver.Chrome(options=chrome_options)
            driver.get(tvShow_url)
            title = driver.find_element(By.CSS_SELECTOR, '.title.ott_true').find_element(By.TAG_NAME, 'h2').find_element(By.TAG_NAME, 'a').text    #for this we got nan values in title of book_url_scraper.py file
            
            overview = driver.find_element(By.CLASS_NAME, "overview").text
            overview = overview.replace("\n", "")    #removes all newline characters (\n) from the string description
            genres = driver.find_element(By.CLASS_NAME, "genres").text

            tvShow_data.append({
                "Url": tvShow_url,
                "Title": title,
                "Overview": overview,
                "Genres": genres
            })

            driver.close()   
            df = pd.DataFrame(data=tvShow_data, columns = tvShow_data[0].keys())
            df.to_csv("TMDB_tv_details.csv", index=False)
            
        except:
            time.sleep(2) 


        
        


        







        
        


        


