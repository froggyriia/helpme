import asyncio
import aiohttp
from random import random
from time_measure_decorator import time_measure
import os
for file in os.listdir('cats'):
    os.remove('cats/'+file)

async def download_cat(session: aiohttp.ClientSession, img_url: str, i: int):
    response = await session.get(img_url)
    img = await response.read()

    frmt = img_url.rsplit('.')[-1]
    file = open(f'cats/cat{i + 1}.{frmt}', 'wb')
    file.write(img)
    file.close()

    print(f"cat {i + 1}.jpg")


async def request():
    link = 'https://api.thecatapi.com/v1/images/search?limit=10'
    session = aiohttp.ClientSession()
    response = await session.get(link)
    answer: list[dict[str, str | int]] = await response.json()
    tasks = []
    for i in range(10):
        img_url = answer[i]['url']
        tasks.append(download_cat(session,img_url, i))
    await asyncio.gather(*tasks)

    await session.close()


@time_measure
def main():
    asyncio.run(request())


main()
