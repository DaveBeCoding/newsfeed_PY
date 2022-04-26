from bs4 import BeautifulSoup

with open('test.html', 'r', encoding="utf-8") as page:
    # soup = BeautifulSoup( page, 'html.parser')
    soup2 = BeautifulSoup(str(page.readlines()), "html.parser")
    print(type(soup2))
    print(soup2)
    # d_page = soup.read()
    # print(d_page)
    # for line in d_page:
    #     # title = line.find('div', {'class': 'img-block'}).text
    #     title = line.find('div', {'class': 'img-block'}).text
    #     # title = line.find('div').text
    #     print(title)



# # Open the saved file
# with open(savefilename, "r", encoding="utf-8") as f:
#     soup2 = BeautifulSoup(str(f.readlines()), "html.parser")
    
# >>> print(type(soup2))
# class 'bs4.BeautifulSoup'>