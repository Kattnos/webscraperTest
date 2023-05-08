from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import webbrowser
import tkinter as tk

file = open('companyNames.txt')
companyFile = file.readlines()

root=tk.Tk()
root.geometry('900x700')

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

def print_url(selectedArticle):
    article = int(selectedArticle) - 1
    print(articles[article].url)

def print_company(selectedArticle):
    article = int(selectedArticle) - 1
    print(articles[article].company)

class article:
    def __init__(self, title, company , content, button, url):
        self.title = title
        self.company = company
        self.content = content
        self.button = button
        self.url = url

articles = []
def refresh_articles():
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

            # button.click()
            # driver.switch_to.window(driver.window_handles[1])
            # url = driver.current_url
            # driver.close()
            # driver.switch_to.window(driver.window_handles[0])

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

            visibleInt = x - 1
            listInt = x - 2

            print(f'{visibleInt}: {articles[listInt].title}')
            print(len(articles))
            print(len(titleText))
            titleText[listInt].config(text=articles[listInt].title)


ser = Service(r"C:\Users\05SIHAB\Documents\chromedriver")
#ser = Service(r"C:\Dev\Python\webscraperTest\chromedriver")
#ser = Service(r'C:\Users\Simon Hagelin\PycharmProjects\webscraperTest\chromedriver')

op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
driver.get(url)
refuseCookiesButton = '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div/div/button'
driver.find_element(by=By.XPATH, value=refuseCookiesButton).click()

articleSelectField = tk.Frame(root)
titleText = []
titleButton = []

for article in articles:
   titleText.append(tk.Label(articleSelectField))
   titleButton.append(tk.Button(articleSelectField, text='Read Article'))

inputField = tk.Frame(root)
programTitle = tk.Label(inputField, text='Retrieve and read articles from Google News', font=('Arial', 16))
refreshButton = tk.Button(inputField, text='Refresh', font=('Arial', 14), command=refresh_articles)

outputFieldFrame = tk.Frame(root)
outputField = tk.Text(outputFieldFrame, font=('Arial', 12))

for title in titleText:
    title.grid(column=0,row=(titleText.index(title)), pady=3)
for button in titleButton:
    button.grid(column=1, row=(titleButton.index(button)),pady=3)

programTitle.pack(pady=10)
refreshButton.pack(pady=5)

inputField.pack(pady=10,padx=2)
articleSelectField.pack(pady=5,padx=5)
outputFieldFrame.pack(pady=20,padx=10)
outputField.pack(side =tk.LEFT, fill = tk.BOTH)

scroll = tk.Scrollbar(outputFieldFrame, orient='vertical', command=outputField.yview)
outputField.config(yscrollcommand=scroll.set)
scroll.pack(side=tk.RIGHT, fill='y')

root.mainloop()

refresh_articles()