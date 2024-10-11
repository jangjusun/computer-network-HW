
# solution 1
# pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
 

url = "https://cau-cpss.github.io/ComputerNetwork/danger/rollingress.html"

# 크롬 드라이버 자동 종료 방지 옵션 추가
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 크롬 드라이버 객체 생성 후 해당 URL 요청
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# 10000번 클릭 반복
for _ in range(10_000):
    driver.find_element("id", "rrlogo").click()
    # alert 확인 버튼 클릭 자동화
    alert = Alert(driver)
    alert.accept()

