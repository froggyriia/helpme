import aiohttp
import asyncio
import os

def get_tasks(data, session): # функция для сбора всех корутин воедино
    tasks = []
    for i in range(10):
        img_url = data[i]["url"]
        img_info = session.get(img_url)
        tasks.append(img_info)
    return tasks
async def download_cats():
    async with aiohttp.ClientSession() as session: # для работы с aiohttp
        url = "https://api.thecatapi.com/v1/images/search?limit=10"
        response = await session.get(url) # делаем запрос на get
        data = await response.json() # преобразуем ответ, тоже через await, чтобы дальше не пошёл
        if not os.path.exists("cats"):
             os.makedirs("cats")
        responses = await asyncio.gather(*get_tasks(data, session)) # запускаем все корутины при помощи gather (звездочка, чтобы раскрыть с
        for i in range(len(responses)): # теперь у нас список готовых ответов, можем по ним пройтись
            response_in_bytes = await responses[i].read()
            with open(f"cats/cat{i}.jpg", "wb") as handler:
                handler.write(response_in_bytes)
        print("Downloaded 10 cat images successfully!")

asyncio.run(download_cats())