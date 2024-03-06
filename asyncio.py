import aiohttp
import asyncio
import time

async def asynchronous_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def async_main():
    urls = [f'https://jsonplaceholder.typicode.com/posts/{i}' for i in range(1, 101)]
    
    start_time = time.time()

    tasks = [asynchronous_request(url) for url in urls]
    results = await asyncio.gather(*tasks)

    end_time = time.time()

    print(f"Asynchronous execution time: {end_time - start_time} seconds")

    return results

asyncio.run(async_main())
