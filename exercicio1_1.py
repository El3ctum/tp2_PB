import aiohttp
import asyncio
import time
import matplotlib.pyplot as plt

async def download_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main(urls):
    tasks = [download_url(url) for url in urls]
    start_time = time.time()
    results = await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Tempo total para {len(urls)} downloads: {end_time - start_time:.2f} segundos")
    return end_time - start_time

base_url = "http://example.com"
num_tasks = [1, 2, 4, 8, 16]
times = []

for n in num_tasks:
    urls = [base_url] * n
    times.append(asyncio.run(main(urls)))

plt.plot(num_tasks, times, marker='o')
plt.xlabel("Número de tarefas concorrentes")
plt.ylabel("Tempo (segundos)")
plt.title("Tempo de Download Assíncrono")
plt.show()