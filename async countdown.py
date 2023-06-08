import asyncio
async def countdown(name: str, n: int, *, sleep_time = 1):
    for i in range(n, -1, -1):
        print(f'{name}: {i}')
        await asyncio.sleep(sleep_time)
    print('countdown is over!')


async def main():
    await asyncio.gather(countdown('for_laundry',10, sleep_time= 0.5), countdown('for_tea', 5, sleep_time= 2))


asyncio.run(main())
