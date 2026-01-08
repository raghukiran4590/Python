from concurrent.futures import ThreadPoolExecutor
import time

def function1(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

if __name__ == "__main__":
    time1 = time.perf_counter()

    tasks = [4, 2, 3]

    with ThreadPoolExecutor() as executor:
        results = executor.map(function1, tasks)
        for result in results:
            print(f"Function completed after {result} seconds")

    time2 = time.perf_counter()

    print(f'Finished in {time2-time1} seconds')