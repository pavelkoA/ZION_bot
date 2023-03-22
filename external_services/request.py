import requests
from bs4 import BeautifulSoup

ssn = requests.Session()
link = 'http://vsdesk/site/login'

data = {
     'LoginForm[username]': 'strike',
     'LoginForm[password]': 'Rfhfv,jkm86',
     'YII_CSRF_TOKEN': 'YmMyfnZobF81NFFveHYyRURtSkw2dnBmaXhRd2diRURbeaMuVK1YMy0Tlm7WpeJ_1YwQsvMbbkjBI-KeIRbgOg%3D%3D',
     'PHPSESSID': 'q8kdl8bahj53d5n9ubl52tcjd5',
     'LoginForm[rememberMe]': '0'
}

s = ssn.post(link, data=data)

# head_dict = {}
# for row in ssn.cookies:
#      head_dict[row.name] = row.value

# # next_page = 'http://vsdesk/request/index?ajax=request-grid-full&Request_page=2'
url = 'http://vsdesk/request/'
req = ssn.get(url=url, headers=data)
print(req.text)