import time
from concurrent.futures import ThreadPoolExecutor

def get_random(n0, n1):
    return f"Random number between {n0} and {n1}"

args_list = [(10, 20), (30, 40), (50, 60)]
print(args_list[0])
print(*args_list)
print(*zip(*args_list))

with ThreadPoolExecutor(max_workers=3) as executor:
    # map() submits the synchronous wrapper function with arguments
    # results = executor.map(get_random, (10, 30, 50), (20, 40, 60))
    results = executor.map(get_random, *zip(*args_list)) # same as above

for r in results:
    print(f"Result: {r}, Time: {time.ctime()}")




