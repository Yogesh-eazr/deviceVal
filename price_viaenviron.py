import re
import requests
import bs4
import pandas as pd

def device_name():
    data = pd.read_json(r'C:\Users\DELL\PycharmProjects\pythonProject2\fuuu.json', typ='series')
    from googlesearch import search
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
    pattern = "flipkart"
    query = data.model
    link_list = []
    model_name_dict = {}
    for j in search(query, num=10, stop=10):
        link_list.append(j)
    for i in range(len(link_list)):
        tt = re.findall(pattern, link_list[i])
        if len(tt) > 0:
            print(link_list[i])
            url = link_list[i]
        else:
            continue
    request_result = requests.get(url)
    soup = bs4.BeautifulSoup(request_result.text,
                             "html.parser")
    dt = soup.find_all('span', class_='B_NuCI')
    for info in dt:
        model_name = info.getText()
    model_name_dict[data.model] = model_name
    return model_name_dict

tt = device_name()
print(tt)



