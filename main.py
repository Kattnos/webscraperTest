from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import webbrowser

def clicking_article(selectedArticle):
    if 1 <= int(selectedArticle) <= 30:
        article = int(selectedArticle) + 1
        driver.find_element(by=By.XPATH,
                            value=f'//*[@id="yDmH0d"]/c-wiz/div/main/c-wiz/div[2]/c-wiz/c-wiz[{article}]/c-wiz/div/article').click()
        driver.switch_to.window(driver.window_handles[1])
        url = driver.current_url
        webbrowser.open_new(url)
        ask_for_input()
    else:
        print('Input does not correspond to an article')


def ask_for_input():
    selectedArticle = input("Select article to open or type 'exit' to exit")
    if selectedArticle != 'exit':
        clicking_article(selectedArticle)

class article:
    def __init__(self, title, company , content, button):
        self.title = title
        self.company = company
        self.content = content
        self.button = button

#ser = Service(r"C:\Users\05SIHAB\Documents\chromedriver")
ser = Service(r"C:\Dev\Python\webscraperTest\chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
driver.get(url)
refuseCookiesButton = '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div/div/button'
driver.find_element(by=By.XPATH, value=refuseCookiesButton).click()

articles = []

for x in range(2, 22):
     news_path = f'//*[@id="yDmH0d"]/c-wiz/div/main/c-wiz/div[2]/c-wiz/c-wiz[{x}]/c-wiz/div/article/h4'
     buttonPath = f'//*[@id="yDmH0d"]/c-wiz/div/main/c-wiz/div[2]/c-wiz/c-wiz[{x}]/c-wiz/div/article'
     try:
         title = driver.find_element(by=By.XPATH, value=news_path)
     except:
         news_path = f'//*[@id="yDmH0d"]/c-wiz/div/main/c-wiz/div[2]/c-wiz/c-wiz[{x}]/c-wiz/article/div[1]/div[2]/div/h4'
         buttonPath = f'//*[@id="yDmH0d"]/c-wiz/div/main/c-wiz/div[2]/c-wiz/c-wiz[{x}]/c-wiz/article/div[1]/div[1]/a'
     finally:
        title = driver.find_element(by=By.XPATH, value=news_path)
        button = driver.find_element(by=By.XPATH, value=buttonPath)

        button.click()
        driver.switch_to.window(driver.window_handles[1])
        url = driver.current_url
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        articles.append(article(title.text,'dsfs','fsdfs' , button))

        visibleInt = x-1
        listInt = x-2

        print(f'{visibleInt}: {articles[listInt].title}')

ask_for_input()
