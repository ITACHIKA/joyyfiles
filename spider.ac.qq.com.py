import requests
from bs4 import BeautifulSoup
import pandas as pd

file=open("result.txt","w")

url = "https://ac.qq.com/Rank" 
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
print(requests.utils.default_user_agent())
response = requests.get(url,headers=headers)
content = response.text

print(content)

soup = BeautifulSoup(content, "html.parser")
data = soup.find("div", id="month_ticket_rank_content")
last_week=data.find_all("div",id="prev-monthticket-rank") #remove last week rank
for item in last_week:
    item.decompose()
ranking=data.find_all("sub") #detailed contents
name=data.find_all("a")
votes=data.find_all("span")
for i in range (len(ranking)):
    ranking[i]=ranking[i].text
    name[i]=name[i].text
    votes[i]=votes[i].text

print(ranking)
print(name)
print(votes)

result={
    "Rank:":ranking,
    "Name:":name,
    "Votes:":votes
}

df=pd.DataFrame(result)
print(df)

df.to_excel("result.xlsx")