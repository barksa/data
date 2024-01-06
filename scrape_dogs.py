from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

# 크롬 드라이버 경로 설정
chrome_driver_path = "C:\\Program Files\\ChromeDriver\\chromedriver.exe"

# 크롬 드라이버 옵션 설정
chrome_options = webdriver.ChromeOptions()
# chromedriver가 돌아가는 창을 숨길 것인지 여부
# chrome_options.add_argument("--headless")  

# 크롬 드라이버 실행
driver = webdriver.Chrome(options=chrome_options)

def scrape_petfinder(url, num_pages):
    # 강아지 정보를 저장할 리스트
    dog_data = []

    driver.get(url)
    time.sleep(1)

    # 강아지 정보가 포함된 HTML 요소 찾기
    dog_elements = driver.find_elements(By.CLASS_NAME, 'petCard_searchResult')

    # 각각의 강아지 정보 추출
    for dog_element in dog_elements:
        img_src = dog_element.find_element(By.CLASS_NAME, 'petCard-media').get_attribute('src')

        # 이름과 종 정보 추출
        name = dog_element.find_element(By.CSS_SELECTOR, '.petCard-body-details-hdg > span').text.strip()

        breed = dog_element.find_element(By.CSS_SELECTOR, 'pf-truncate').text.strip()

        # 이름, 종, 이미지 소스 중 하나라도 공백이 있으면 dog_data에 추가하지 않음
        if not (name and breed and img_src):
            continue

        # 추출한 정보를 딕셔너리로 저장
        dog_info = {
            'Image Source': img_src,
            'Name': name,
            'Breed': breed
        }

        # 딕셔너리를 리스트에 추가
        dog_data.append(dog_info)

    # 페이지가 로딩되기를 기다림 (필요에 따라 조절)
    time.sleep(1)

    try:
        # 2페이지 이후의 페이지들에 대해 위의 과정 반복
        for page in range(1, num_pages + 1):
            # 현재 페이지의 URL 생성
            current_url = f"{url}&page={page}"

            # 크롬드라이버로 페이지 열기
            driver.get(current_url)
            time.sleep(1)

            dog_elements = driver.find_elements(By.CLASS_NAME, 'petCard_searchResult')

            for dog_element in dog_elements:
                img_src = dog_element.find_element(By.CLASS_NAME, 'petCard-media').get_attribute('src')

                name = dog_element.find_element(By.CSS_SELECTOR, '.petCard-body-details-hdg > span').text.strip()

                breed = dog_element.find_element(By.CSS_SELECTOR, 'pf-truncate').text.strip()

                if not (name and breed and img_src):
                    continue

                dog_info = {
                    'Image Source': img_src,
                    'Name': name,
                    'Breed': breed
                }

                dog_data.append(dog_info)
            time.sleep(1)

    finally:
        # 크롬드라이버 종료
        driver.quit()

    return dog_data

def save_to_csv(data, filename='dog_data.csv'):
    with open(filename, mode='w', encoding='utf-8', newline='') as csv_file:
        fieldnames = ['Image Source', 'Name', 'Breed']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # CSV 파일 헤더 쓰기
        writer.writeheader()

        # 강아지 정보 쓰기
        for dog_info in data:
            writer.writerow(dog_info)

if __name__ == "__main__":
    base_url = "https://www.petfinder.com/search/dogs-for-adoption/gu/piti-municipality/?distance=Anywhere"

    num_pages_to_scrape = 3  # 원하는 페이지 수

    dog_data = scrape_petfinder(base_url, num_pages_to_scrape)
    save_to_csv(dog_data)

    print(f'Dog data has been scraped and saved to dog_data.csv')