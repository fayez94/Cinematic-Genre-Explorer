from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm
import pandas as pd
import time


if __name__ == "__main__":
    # Initialize the webdriver
    driver = webdriver.Chrome()
    base_url = "https://www.themoviedb.org/movie?language=en-US"
    time.sleep(5)  

    movies = []

    print("Scraping movies...")
    for idx in tqdm(range(500)):
        page_no = idx + 1
        page_url = f"{base_url}&page={page_no}"
        driver.get(page_url)

        # Find all movie items under the current page
        movie_items = driver.find_elements(By.CSS_SELECTOR, ".card.style_1" )
        for movie in movie_items:
            try:
                heading = movie.find_element(By.TAG_NAME, "h2")
                url_tag = heading.find_element(By.TAG_NAME, "a")
                title = url_tag.get_attribute("title")
                movie_url = url_tag.get_attribute("href")
                movies.append({"title": title, "Url":movie_url })
            except Exception as e:
                print(f"Skipping an item due to error: {e}")
        


# Save data to CSV after each load
df = pd.DataFrame(movies)
df.to_csv("tmdb_movies.csv", index=False)

# Close the browser
driver.quit()

print("Scraping completed. Data saved to 'tmdb_movies.csv'.")
