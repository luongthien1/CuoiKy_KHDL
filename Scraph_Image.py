from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
import os
names = ["Elon Musk", "Jeff Bezos", "Dwayne Johnson", "Emma Watson", "Kylian Mbappe", "Vladimir Vladimirovich Putin", "Donald Trump",
	 "Bill Gates", "James Patterson", "George Clooney", "Mark Zuckerberg", "Judy Sheindlin", "Lionel Messi", "Barack Obama", "Mark Zuckerberg",
	 "Justin Bieber", "Kim Jong Un", "Joe Biden", "Angela Merkel", "Bernard Arnault"]
def crawl():
	# for name in names:
	for i in range(1):
		name = names[-1]
		para = {}
		para["1"] = name.lower().replace(" ", "-")
		para["2"] = name.replace(" ", "%20")

		path_folder = f"dataset/{name}"
		if not os.path.exists(path_folder):
			os.makedirs(path_folder)

		count = 0
		for i in range(1, 100):
			print(i)
			headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"}
			req = requests.get(f"https://www.gettyimages.com/photos/{para['1']}?assettype=image&family=editorial&phrase={para['2']}&sort=mostpopular&page={i}", headers=headers)  # URL of the website which you want to scrape
			content = req.content  # Get the content
			soup = BeautifulSoup(content, 'html.parser')
			imgs = soup.select("picture > source")
			
			for img in imgs :
				url_img = img.attrs["srcset"]
				print(count+1, url_img)

				response = requests.get(url_img)
				if response.status_code != 404:
					count +=1
					fp = open(f'dataset/{name}/{count}.jpg', 'wb')
					fp.write(response.content)
					fp.close()
			if count > 700:
				break
	save()

def save():
	pass

if __name__ == '__main__':
	crawl()