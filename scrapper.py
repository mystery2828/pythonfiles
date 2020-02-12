import requests
from bs4 import BeautifulSoup
import smtplib
import time

#URL = 'https://www.amazon.in/Ambrane-10000mAh-Lithium-Polymer-Capsule-10K/dp/B07S88FHN6/ref=sr_1_1?qid=1574356033&refinements=p_89%3AAmbrane&s=electronics&sr=1-1'
URL = 'https://www.amazon.in/Philips-Trimmer-Cordless-Corded-QT4011/dp/B00JJIDBIC/ref=pd_sbs_364_t_0/261-9040355-0798036?_encoding=UTF8&pd_rd_i=B00JJIDBIC&pd_rd_r=37f31cb0-ba19-4a94-a09b-4887c719612e&pd_rd_w=EK8kw&pd_rd_wg=nXtZc&pf_rd_p=21bbdc4d-873b-48c5-a88a-70e643377944&pf_rd_r=REWTMXE62Z70Z7EBKF9P&psc=1&refRID=REWTMXE62Z70Z7EBKF9P'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}


def check_price():

    page  = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    #title = soup.find(classmethod='_35KyD6').get_text()
    title = soup.findAll("span", class_= "_35KyD6")
    price = soup.findAll("span",class_='_1vC4OE _3qQ9m1')
    #converted_price = (price[2:7])
    print(price)
    # if converted_price > 499:
    #     send_mail()
    # print(title.strip())



def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('akashindeekshainiit@gmail.com','icmvqrepfllnwmky')

    subject = 'Price fell down'
    #body = 'Check the amazon Link https://www.amazon.in/Ambrane-10000mAh-Lithium-Polymer-Capsule-10K/dp/B07S88FHN6/ref=sr_1_1?qid=1574356033&refinements=p_89%3AAmbrane&s=electronics&sr=1-1'
    body = ' check the link https://www.amazon.in/Philips-Trimmer-Cordless-Corded-QT4011/dp/B00JJIDBIC/ref=pd_sbs_364_t_0/261-9040355-0798036?_encoding=UTF8&pd_rd_i=B00JJIDBIC&pd_rd_r=37f31cb0-ba19-4a94-a09b-4887c719612e&pd_rd_w=EK8kw&pd_rd_wg=nXtZc&pf_rd_p=21bbdc4d-873b-48c5-a88a-70e643377944&pf_rd_r=REWTMXE62Z70Z7EBKF9P&psc=1&refRID=REWTMXE62Z70Z7EBKF9P'
    msg = f"Subject: {subject} \n\n{body}"

    server.sendmail(
        'akashindeekshainiit@gmail.com',
        'muralitheboss99@gmail.com',
        msg
    )
    print('Hey mail sent')
    server.quit()

while(True):

    check_price()
    time.sleep(3600)