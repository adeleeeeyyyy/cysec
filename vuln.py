import requests
from bs4 import BeautifulSoup

def check_sql_injection(url):
    test_payload = "' OR '1'='1"
    response = requests.get(f"{url}?id={test_payload}")
    if "error" not in response.text.lower():
        print("Potential SQL Injection vulnerability found!")
    else:
        print("No SQL Injection vulnerability found.")

url = "http://example.com/page"
check_sql_injection(url)
