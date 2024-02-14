from multiprocessing import  Pool,  cpu_count, current_process
import time

def factorize(numbers):
    #start_time = time.time()

    list = []

    for num in numbers:
        values = []
        for el in range(1, num+1):
            if num % el == 0:
                values.append(el)
        list.append(values)

    #Синхронна версія та час вмконання
    #end_time = time.time()
    #execution_time = end_time - start_time
    #print(f"Execution time: {execution_time} seconds")
    return list
def callback(result):
    print(result.upper())

if __name__ == "__main__":
    #numbers = [12, 14, 16, 18, 20]
    #result = factorize(numbers)
    #print(result)
    # Асинхронна версія
    print(f'count CPU: {cpu_count()}')
    with Pool(cpu_count()) as p:
        p.map_async(factorize, [128, 255, 99999, 10651060], callback=callback)
        # !! колбек викличеться для кінцевого числа. колбек увімкнеться як мапінг завершить роботу. результат ми отримаємо в самому кінці
        p.close()  # перестати виділяти процеси в пул
        p.join()
    print(f'end {current_process().name}')



