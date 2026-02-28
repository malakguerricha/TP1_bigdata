# مسؤول غير على جلب الصفحة

import requests

def fetch_page(url, headers):
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.text