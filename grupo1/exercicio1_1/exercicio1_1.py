import asyncio
import aiohttp
import time
import matplotlib.pyplot as plt


async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()


async def download_urls(urls, num_concurrent):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results


async def main():
    urls = ["https://example.com", "https://httpbin.org/get",
            "https://jsonplaceholder.typicode.com/posts"] * 10

    num_concurrent_list = [1, 2, 5, 10, 20, 50]
    times = []

    for num_concurrent in num_concurrent_list:
        start_time = time.time()
        await download_urls(urls[:num_concurrent], num_concurrent)
        end_time = time.time()
        times.append(end_time - start_time)
        print(f"Tempo para {num_concurrent} downloads: {
              end_time - start_time:.2f} segundos")

    # Plotando o gráfico
    plt.plot(num_concurrent_list, times, marker='o')
    plt.xlabel('Número de Downloads Simultâneos')
    plt.ylabel('Tempo Total (segundos)')
    plt.title('Número de Downloads Simultâneos x Tempo Total')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    asyncio.run(main())
