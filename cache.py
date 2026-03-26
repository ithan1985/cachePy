import time
from functools import lru_cache

@lru_cache(maxsize=4)
def task(a=0, b=0):
    print(f"Calculando task({a}, {b}) ... operación costosa")
    time.sleep(2)
    return a + b

start = time.time()

print("1:", task(10, 20))   # MISS
print("2:",task(10, 20))   # HIT
print("3:",task(10, 20))   # HIT
print("4:",task(10, 25))   # MISS
print("5:",task(10, 25))   # HIT

print(task.cache_info())

print(f"Tiempo total: {time.time() - start:.2f} segundos")