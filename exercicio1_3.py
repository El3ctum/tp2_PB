import asyncio
from PIL import Image, ImageFilter
import os
import time
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor


def aplicar_filtro(imagem_path, output_path):
    with Image.open(imagem_path) as img:
        img_filtrada = img.filter(ImageFilter.BLUR)
        img_filtrada.save(output_path)


async def processar_imagem(imagem_path, output_path):
    await asyncio.to_thread(aplicar_filtro, imagem_path, output_path)


async def main(max_workers, imagens):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        loop = asyncio.get_running_loop()
        start_time = time.time()
        tasks = [loop.run_in_executor(
            executor, aplicar_filtro, img, f"imagensProcessadas/{os.path.basename(img)}") for img in imagens]
        await asyncio.gather(*tasks)
        return time.time() - start_time

pasta_imagens = "imagens"
imagens = [os.path.join(pasta_imagens, f) for f in os.listdir(
    pasta_imagens) if f.endswith(('.png', '.jpg'))]
workers_list = [1, 2, 4, 8]
times = []
for workers in workers_list:
    tempo = asyncio.run(main(workers, imagens))
    times.append(tempo)
    print(f"Workers: {workers}, Tempo: {tempo:.2f}s")

plt.plot(workers_list, times, marker='o')
plt.xlabel("Número de threads")
plt.ylabel("Tempo (segundos)")
plt.show()
