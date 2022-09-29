# importing libraries
from turtle import color
from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *

root = Tk()
root.title("Comparing Products")
root.geometry("500x500+20+20")
root.config(bg="#00bfff") 
uc = u"\u20B9"
uc = u"\u20B9"
# Function to extract Product Title






def flipkart(url2):
	HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
	webpage = requests.get(url2, headers=HEADERS)
	soup = BeautifulSoup(webpage.content, "lxml")
	def get_title(soup):
	
		try:
			# Outer Tag Object
			title = soup.find("span",{"class":"B_NuCI"}).get_text()

			# Inner NavigableString Object
			# title_value = title.string

			# Title as a string value
			title_string = title.strip()

		except AttributeError:
			title_string = ""	

		return title_string

	# Function to extract Product Price

	def get_price(soup):

		try:
			price = soup.find("div",{"class":"_30jeq3 _16Jk6d"}).get_text()
		except AttributeError:
			price = ""	

		return price

	# Function to extract Product Rating
	def get_rating(soup):

		try:
			# Outer Tag Object
			rating = soup.find("div",{"class": "_2d4LTz"}).get_text()

			# Inner NavigableString Object
			# title_value = title.string

			# Title as a string value
			rating_string = rating.strip()

		except AttributeError:
			rating_string = ""	

		return rating_string	

	# Function to extract Number of User Reviews
	def get_review_count(soup):
		try:
			review_count = soup.find("span",{"class":"_2_R_DZ"}).get_text()
		except AttributeError:
			review_count = ""	

		return review_count

# Function to extract Availability Status
	def get_availability(soup):
		try:
			available = soup.find("div", {'class':'_16FRp0'}).get_text()
			# available = available.find("span").string.strip()
		
		except AttributeError:
			available = "Available"	

	# if available != "Sold Out":
	# 		available = "Available"
	# 		return available
	# else:
		return available
	print()
	print("Flipkart")
	print(get_title(soup))
	print(get_price(soup))
	print(get_rating(soup))
	print(get_review_count(soup))
	print(get_availability(soup))
	print()
	print("---------------------------------------------------------------------------------------")
	













def amazon(url1):
	
	HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
	webpage = requests.get(url1, headers=HEADERS)
	soup = BeautifulSoup(webpage.content, "lxml")
	

	def get_title(soup):
	
		try:
			# Outer Tag Object
			title = soup.find("span", attrs={"id":'productTitle'})

			# Inner NavigableString Object
			title_value = title.string

			# Title as a string value
			title_string = title_value.strip()

		except AttributeError:
			title_string = ""	

		return title_string

# Function to extract Product Price

	def get_price(soup):

		try:
			price = soup.find("span", attrs={'class':'a-offscreen'}).string.strip()
		except AttributeError:
			price = ""	

		return price

# Function to extract Product Rating
	def get_rating(soup):

		try:
			rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
		except AttributeError:
		
			try:
				rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
			except:
				rating = ""	

		return rating

# Function to extract Number of User Reviews
	def get_review_count(soup):
		try:
			review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
		except AttributeError:
			review_count = ""	

		return review_count

# Function to extract Availability Status
	def get_availability(soup):
		try:
			available = soup.find("div", attrs={'id':'availability'})
			available = available.find("span").string.strip()
		except AttributeError:
			available = ""	

		return available
	print()
	print("Amazon")
	print(get_title(soup))
	print(get_price(soup))
	print(get_rating(soup))
	print(get_review_count(soup))
	print(get_availability(soup))
	print("---------------------------------------------------------------------------------------")
	

def get_link():
	# Headers for request
	url1 = ent_ama.get()
	url2 = ent_flk.get()
	flipkart(url2)
	
	amazon(url1)
 

f1 = ("Times New Roman", 25, "bold")
f2 = ("Times New Roman", 18 )
f3 = ("Times New Roman", 20)

ama_url = Label(root, text = "Enter URL From Amazon", font = f3, bg="aqua", fg="black")
ama_url.pack(pady=10)
ent_ama = Entry(root, font = f2, fg="blue" )
ent_ama.pack()

ama_flk = Label(root, text = "Enter URL From Flipkart", font = f3, bg="aqua", fg="black")
ama_flk.pack(pady=10)
ent_flk = Entry(root, font = f2, fg="blue")
ent_flk.pack()

btn_sub = Button(root, text = "Compare", font = f1, fg="darkblue",command = get_link)
btn_sub.pack(pady=30)

root.mainloop()


