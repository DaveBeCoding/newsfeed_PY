# from turtle import title
from bs4 import BeautifulSoup

with open('test.html', 'r', encoding="utf-8") as page:
    # soup = BeautifulSoup( page, 'html.parser')
    soup2 = BeautifulSoup(str(page.readlines()), "html.parser")
    
    questions = soup2.find_all('div', {'class' : 'display-desktop-none'})
    # questions = soup2.a
    # print(len(questions))
    # title = questions.find('a', {'class': 'category'})
    for items in questions:
        item = items.string
        # title = item.find("a", {"class": "category", "href": True})['href']
        # print(item)
        # title = item.find('p')
        # print(title)
        # title = item.find('p', {'class': 'typography__StyledTypography-owin6q-0'})
        # title = item.find('a', {'class': 'category'})
        print(item)
    
    
    # print(type(soup2))
    # print(soup2)
    # d_page = soup2.read()
    # print(d_page)
    # for line in soup2:
        # print("the line", line)
        # title = line.find('div', {'class': 'img-block'}).text()
        # title = line.find('div', {'class': 'img-block'})
        # title = line.find('div')
        # print(title)



# # Open the saved file
# with open(savefilename, "r", encoding="utf-8") as f:
#     soup2 = BeautifulSoup(str(f.readlines()), "html.parser")
    
# >>> print(type(soup2))
# class 'bs4.BeautifulSoup'>

# update test-branch to main ::
# git fetch 
# git rebase [main]

# history Display last n lines
# history [n n*] (start-n end-n*) -> first (n's)

# last [n n*]
# history [-n -n*] -> last (-n's)
