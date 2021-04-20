import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import *
import re
from flask import jsonify, Flask, request

app = Flask(__name__)

##pip install google


# driver = webdriver.Chrome(ChromeDriverManager().install())
#
# data = pd.read_json(r'C:\Users\DELL\PycharmProjects\pythonProject2\huuu.json', typ='series')
# print(data)
#
# pattern = "flipkart"
#
# from googlesearch import googlesearch
#
# try:
#     from googlesearch import search
# except ImportError:
#     print("No module named 'google' found")
# link_list = []
# query = data.model
#
# ### Getting url list
#
# for j in search(query, tld="co.in", num=10, stop=10):
#     link_list.append(j)
#
# for i in range(len(link_list)):
#     tt = re.findall(pattern,link_list[i])
#     if len(tt)>0:
#         print(link_list[i])
#         url = link_list[i]
#     else:
#         continue
#
# driver.get(f'{url}')
#
# sleep(2)
# model_name = driver.find_element_by_css_selector(".B_NuCI")
# modname = model_name.text
# print(model_name.text)
# price = driver.find_elements_by_css_selector("._30jeq3._16Jk6d")
# # print(price)
# # print(len(price))
# pp = price[0].text
# print("SOLD AT PRICE",pp)
# driver.close()


@app.route("/devicename",methods=['GET'])
def get_mobile_name_and_price():
    final_list = []
    driver = webdriver.Chrome(ChromeDriverManager().install())
    data = pd.read_json(r'C:\Users\DELL\PycharmProjects\pythonProject2\huuu.json', typ='series')
    pattern = "flipkart"
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
    link_list = []
    query = data.model
    for j in search(query, tld="co.in", num=10, stop=10):
        link_list.append(j)

    for i in range(len(link_list)):
        tt = re.findall(pattern, link_list[i])
        if len(tt) > 0:
            print(link_list[i])
            url = link_list[i]
        else:
            continue

    # driver.get(f'{url}')
    driver.get(f'{url}')

    sleep(2)
    model_name = driver.find_element_by_css_selector(".B_NuCI")
    modname = model_name.text
    print(model_name.text)
    final_list.append(modname)
    price = driver.find_elements_by_css_selector("._30jeq3._16Jk6d")
    pp = price[0].text
    print("SOLD AT PRICE", pp)
    final_list.append(pp)
    driver.close()
    return jsonify({"Value":final_list})

if __name__=='__main__':
    app.run('localhost', 8082)

# lo = get_mobile_name_and_price()
# print(lo)

