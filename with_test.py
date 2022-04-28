# from turtle import title
from bs4 import BeautifulSoup

with open('test.html', 'r', encoding="utf-8") as page:
    soup2 = BeautifulSoup(str(page.readlines()), "html.parser")

    questions = soup2.find_all('div', {'class': 'display-desktop-none'})
    questions = soup2.a

    # clean-text
    print(str(questions)[2:-4] + "\n")
    print(questions.string)

