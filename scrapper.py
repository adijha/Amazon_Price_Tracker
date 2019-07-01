import requests 
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/gp/product/B01F8LCALM/ref=s9_acsd_top_hd_bw_b1V58sh_c_x_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-12&pf_rd_r=MDE9Y5TPMKG63RF9EYCT&pf_rd_t=101&pf_rd_p=cffea88c-d4b4-54e6-90a1-dc4e077a6e74&pf_rd_i=1375425031'


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
  page = requests.get(URL, headers= headers)

  soup = BeautifulSoup(page.content, 'html.parser')

  title = soup.find(id="productTitle").get_text()
  price = soup.find(id="priceblock_ourprice").get_text()
  converted_price = float(price[2])

  print(converted_price)
  print(title.strip())

  if(converted_price < 8):
    send_mail()

def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('adityajha526@gmail.com', '<your google app password>')

  subject = 'Congrats! Price fell down!'
  body = 'check the amazon link https://www.amazon.in/gp/product/B01F8LCALM/ref=s9_acsd_top_hd_bw_b1V58sh_c_x_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-12&pf_rd_r=MDE9Y5TPMKG63RF9EYCT&pf_rd_t=101&pf_rd_p=cffea88c-d4b4-54e6-90a1-dc4e077a6e74&pf_rd_i=1375425031'

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