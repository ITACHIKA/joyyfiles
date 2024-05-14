import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

file=open("result.txt","w")

url = "https://movie.douban.com/top250" 
headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

movieTitles=[]
scoreRatings=[]
totstars=[]
fivePerc=[]
fourPerc=[]
threePerc=[]
twoPerc=[]
onePerc=[]

for i in range(0,245,25):
    print(i)
    response = requests.get("https://movie.douban.com/top250?start="+str(i)+"&filter=",headers=headers)
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    pictureLinks=soup.find_all("div",class_='hd') #find link to movie on the given page of 25 movies
    
    for divLink in pictureLinks:
        linkToMovie=divLink.find("a")
        print(linkToMovie.get('href'))
        response = requests.get(linkToMovie.get('href'),headers=headers) # access page of single movie
        
        secondLevelPage=BeautifulSoup(response.text,"html.parser")

        detailRating=secondLevelPage.find_all("span",class_="rating_per")
        for i in range(len(detailRating)):
            detailRating[i]=detailRating[i].text
            
        movieTitle= re.sub(r'[\n\r]+', '',secondLevelPage.find("title").text.strip())
        
        scoreRating=secondLevelPage.find("strong",class_="ll rating_num").text #find number rating
        
        level=["50","45","40","35","30","25","20","15","10","5","0"]
        for i in level:
            if(secondLevelPage.find("div",class_=("ll bigstar bigstar"+i))!=None):  #find star rating
                star=i
                break
        print(movieTitle)
        print(scoreRating)
        print(star)
        print(detailRating)
        movieTitles.append(movieTitle)
        scoreRatings.append(scoreRating)
        totstars.append(star)
        fivePerc.append(detailRating[0])
        fourPerc.append(detailRating[1])
        threePerc.append(detailRating[2])
        twoPerc.append(detailRating[3])
        onePerc.append(detailRating[4])
dict={
    "Title":movieTitles,
    "Score":scoreRatings,
    "Star":totstars,
    "Fives":fivePerc,
    "Fours":fourPerc,
    "Threes":threePerc,
    "Twos":twoPerc,
    "Ones":onePerc
}

df=pd.DataFrame(dict)

print(df)

df.to_excel("movies.xlsx")