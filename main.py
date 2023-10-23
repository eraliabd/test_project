# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://road24.uz/'
# response = requests.get(url=url)
# print(response)
# if response.status_code == 200:
#     html_content = response.content
#     soup = BeautifulSoup(html_content, 'html.parser')
#     first_h1 = soup.find('h1').get_text()
#     print(first_h1)
# else:
#     print("Failed to fetch the website.")
# exit()



import functools


# # Decorator to enable caching
# @functools.lru_cache(maxsize=None)  # maxsize=None means unlimited cache size
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# # Test the Fibonacci function
# for i in range(10000):
#     print(f"Fibonacci({i}) = {fibonacci(i)}")


# ML
# pip install XlsxWriter

# import xlsxwriter
# worksheet.write(row, col, 'Hello')
