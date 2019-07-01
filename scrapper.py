import requests 
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sony+alfa+7+ILCE&qid=1561962786&s=gateway&sr=8-1-spons&psc=1'


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
  page = requests.get(URL, headers= headers)

  soup = BeautifulSoup(page.content, 'html.parser')

  title = soup.find(id="productTitle").get_text()
  price = soup.find(id = "priceblock_ourprice").get_text()
  converted_price = float(price[0:5])

  if(converted_price < 1.700):
    send_mail()

  print(converted_price)
  print(title.strip())

  if(converted_price > 1.700):
    send_mail()

def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('adityajha526@gmail.com', 'xpcniufkjtuxsfuj')

  subject = 'Price fell down!'
  body = 'check the amazon link https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sony+alfa+7+ILCE&qid=1561962786&s=gateway&sr=8-1-spons&psc=1'

  msg = f"Subject: {subject}\n\n{body}"

  server.sendmail(
    'adityajha526@gmail.com', 
    'adityajha126@gmail.com',
    msg
  )
  print('Hey email has been sent!')

  server.quit()

while(True):
  check_price()
  time.sleep(3600*24)