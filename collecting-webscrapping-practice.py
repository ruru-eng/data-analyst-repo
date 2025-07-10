from bs4 import BeautifulSoup
import requests

# URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
# data=requests.get(URL).text
# soup=BeautifulSoup(data,"html.parser")
# table=soup.find("table")

# for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
#     # Get all columns in each row.
#     cols = row.find_all('td') # in html a column is represented by the tag <td>
#     color_name = cols[2].getText() # store the value in column 3 as color_name
#     color_code = cols[3].getText() # store the value in column 4 as color_code
#     print("{}--->{}".format(color_name,color_code))

url2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"

# request data from url
data2=requests.get(url2).text
# create a soup object
soup2=BeautifulSoup(data2,"html.parser")
# scrape the *Language name* and *annual average salary*
table2=soup2.find("table")
with open("popular-languages.csv","w") as f:
    for row in table2.find_all("tr"):
        cols=row.find_all("td")
        lang=cols[1].getText()
        sal=cols[3].getText()
        f.write(f"{lang},{sal}\n")

