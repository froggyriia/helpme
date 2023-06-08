import requests
from PIL import Image
import shutil
import os
from time import time

def time_measure(func: callable):
    def wrapper(*args, **kwargs):
        before_execute = time()
        result = func(*args, **kwargs)
        after_execute = time()
        print(f'{func.__name__} was called for {after_execute - before_execute}')
        return result

    return wrapper

@time_measure
def download_cats():


    if not os.path.exists("cats"):
        os.makedirs("cats")
    else:
        shutil.rmtree("cats")
        os.makedirs("cats")

    link = "https://api.thecatapi.com/v1/images/search?limit=10"
    answer: list[dict: str | int] = requests.get(link).json()
# print(answer)
    url_s = []
    for i in answer:
        url_s.append(i.get('url'))

# print(url_s)
    c = 0
    for url in url_s:
        url: str
        frmt = url.rsplit(".")[-1]
        data = requests.get(url).content
        with open(f'cats/cat{c}.{frmt}', "w") as file:
            f = open(f'img{c}.{frmt}', 'wb')
            f.write(data)
            f.close()

        img = Image.open(f'img{c}.{frmt}')
        img.show()
        c += 1
download_cats()