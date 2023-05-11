from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import webbrowser
import tkinter as tk
from newspaper import Article
import time

root=tk.Tk()
root.geometry('1000x900')

companyURL = []
companyFormatted = []

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
    def __init__(self, title , content, button, url):
        self.title = title
        self.content = content
        self.button = button
        self.url = url

articles = []
articleLength = 5

def refresh_articles():
    for x in range(2, (articleLength + 2)):
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

            #for string in companyURL:
            #    searchableURL = url.rpartition('1')[0]
            #    if searchableURL.find(string) != -1:
            #        searchInt = companyURL.index(string)
            #        company = companyFormatted[searchInt].rstrip()
            #        print(company)
            #        break
            #    else:
            #        company = 'Unknown's

            articles.append(article(title.text, 'fsdfs', button, url))
            titleText[x-2].config(text=articles[x-2].title)

def open_article(articleInt):
    print('Opening article ' + str(articleInt))

    articles[articleInt].button.click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(0.5)
    url = driver.current_url
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    accessedArticle=Article(url)
    accessedArticle.download()
    accessedArticle.parse()

    outputField.delete('1.0', tk.END)
    outputField.insert(tk.END, accessedArticle.text)

articleSelectField = tk.Frame(root)
titleText = []
titleButton = []

ser = Service(r"./driver/chromedriver.exe")

op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
driver.get(url)
refuseCookiesButton = '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div/div/button'
driver.find_element(by=By.XPATH, value=refuseCookiesButton).click()

articleSelectField = tk.Frame(root)
titleText = []
titleButton = []

for int in range(0, articleLength):
    titleText.append(tk.Label(articleSelectField))
    print(int)
    titleButton.append(tk.Button(articleSelectField, text='Read Article'))

for int, button in enumerate(titleButton):
    titleButton[int].config(command=lambda int=int: open_article(int))

refresh_articles()

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