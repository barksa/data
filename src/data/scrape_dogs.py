from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

# Set the path for the Chrome driver
chrome_driver_path = "C:\\Program Files\\ChromeDriver\\chromedriver.exe"

# Configure Chrome driver options
chrome_options = webdriver.ChromeOptions()

# Whether to hide the window in which chromedriver runs
# chrome_options.add_argument("--headless")

# Launch the Chrome driver
driver = webdriver.Chrome(options=chrome_options)


def scrape_petfinder(url, num_pages):
    # List to store dog information
    dog_data = []

    driver.get(url)
    time.sleep(1)

    # Find HTML elements containing dog information
    dog_elements = driver.find_elements(By.CLASS_NAME, "petCard_searchResult")

    # Extract information for each dog
    for dog_element in dog_elements:
        img_src = dog_element.find_element(
            By.CLASS_NAME, "petCard-media"
        ).get_attribute("src")

        # Extract name and breed information
        name = dog_element.find_element(
            By.CSS_SELECTOR, ".petCard-body-details-hdg > span"
        ).text.strip()

        breed = dog_element.find_element(By.CSS_SELECTOR, "pf-truncate").text.strip()

        # Do not add to dog_data if name, breed, or image source contains a blank.
        if not (name and breed and img_src):
            continue

        # Store the extracted information in a dictionary
        dog_info = {"Image Source": img_src, "Name": name, "Breed": breed}

        # Add the dictionary to the list
        dog_data.append(dog_info)

    # Wait for the page to load (adjust as needed)
    time.sleep(1)

    try:
        # Repeat the above process for pages beyond page 1
        for page in range(1, num_pages + 1):
            # Create the URL for the current page
            current_url = f"{url}&page={page}"

            # Open the page with the Chrome driver
            driver.get(current_url)
            time.sleep(1)

            dog_elements = driver.find_elements(By.CLASS_NAME, "petCard_searchResult")

            for dog_element in dog_elements:
                img_src = dog_element.find_element(
                    By.CLASS_NAME, "petCard-media"
                ).get_attribute("src")

                name = dog_element.find_element(
                    By.CSS_SELECTOR, ".petCard-body-details-hdg > span"
                ).text.strip()

                breed = dog_element.find_element(
                    By.CSS_SELECTOR, "pf-truncate"
                ).text.strip()

                if not (name and breed and img_src):
                    continue

                dog_info = {"Image Source": img_src, "Name": name, "Breed": breed}

                dog_data.append(dog_info)
            time.sleep(1)

    finally:
        # Quit the Chrome driver
        driver.quit()

    return dog_data


def save_to_csv(data, filename="dog_data.csv"):
    with open(filename, mode="w", encoding="utf-8", newline="") as csv_file:
        fieldnames = ["Image Source", "Name", "Breed"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write CSV file header
        writer.writeheader()

        # Write dog information to the file
        for dog_info in data:
            writer.writerow(dog_info)


if __name__ == "__main__":
    base_url = "https://www.petfinder.com/search/dogs-for-adoption/gu/piti-municipality/?distance=Anywhere"

    num_pages_to_scrape = 3  # Desired number of pages for scraping

    dog_data = scrape_petfinder(base_url, num_pages_to_scrape)
    save_to_csv(dog_data)

    print(f"Dog data has been scraped and saved to dog_data.csv")
