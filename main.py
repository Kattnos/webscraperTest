from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import webbrowser

file = open('companyNames.txt')
companyFile = file.readlines()

companyURL = []
companyFormatted = []
for line in companyFile:
    companyURL.append(line.partition('-')[0])
    string = line.partition('-')[2]
    companyFormatted.append(string)
print(companyURL)

def clicking_article(selectedArticle):
    article = int(selectedArticle) - 1
    webbrowser.open_new(articles[article].url)
    ask_for_input()


def print_url(selectedArticle):
    article = int(selectedArticle) - 1
    print(articles[article].url)
    ask_for_input()

def print_company(selectedArticle):
    article = int(selectedArticle) - 1
    print(articles[article].company)
    ask_for_input()


def ask_for_input():
    selectedInput = input("Enter a command or type 'help'")

    if selectedInput == 'help':
        print('Available commands: \n articleNumber.open \n articleNumber.company \n articleNumber.url \n exit')
        ask_for_input()
    if selectedInput == 'exit':
        return

    subCommand = selectedInput.rpartition('.')[2]
    selectedArticle = selectedInput.rpartition('.')[0]

    try:
        selectedInt = int(selectedArticle)
    except:
        print('Unknown command')
        ask_for_input()
    if 5 >= selectedInt >= 1:
        match subCommand:
            case 'open':
                clicking_article(selectedInt)
            case 'url':
                print_url(selectedInt)
            case 'company':
                print_company(selectedInt)
            case _:
                print('Unknown command')
        ask_for_input()
    else:
        print('Article not found')
        ask_for_input()

class article:
    def __init__(self, title, company , content, button, url):
        self.title = title
        self.company = company
        self.content = content
        self.button = button
        self.url = url

ser = Service(r"C:\Users\05SIHAB\Documents\chromedriver")
#ser = Service(r"C:\Dev\Python\webscraperTest\chromedriver")
#ser = Service(r'C:\Users\Simon Hagelin\PycharmProjects\webscraperTest\chromedriver')

op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
driver.get(url)
refuseCookiesButton = '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div/div/button'
driver.find_element(by=By.XPATH, value=refuseCookiesButton).click()

articles = []

for x in range(2, 7):
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

        for string in companyURL:
            searchableURL = url.rpartition('1')[0]
            if searchableURL.find(string) != -1:
                searchInt = companyURL.index(string)
                company = companyFormatted[searchInt].rstrip()
                print(company)
                break
            else:
                company = 'Unknown'

        articles.append(article(title.text, company, 'fsdfs', button, url))

        visibleInt = x-1
        listInt = x-2

        print(f'{visibleInt}: {articles[listInt].title}')

ask_for_input()
