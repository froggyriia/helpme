from time import sleep
MLTPR = 3
import asyncio
async def laundary():
    print('Поставили стирку')
    await asyncio.sleep(1 * MLTPR)
    print('Стирка закончена')

async def cooking():
    print('Поставили щи')
    await asyncio.sleep(1 * MLTPR)
    print('Щи готов')


async def tea():
    print('Ставим чайнки')
    await asyncio.sleep(0.15 * MLTPR)
    print('Пьем чай')

async def main():
    await asyncio.gather(laundary(), cooking(), tea())



asyncio.run(main())