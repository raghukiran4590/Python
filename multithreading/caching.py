from functools import lru_cache
import threading
import time

@lru_cache(maxsize=128)
def expensive_computation(x):
    """Simulates an expensive computation by sleeping."""
    time.sleep(2)  # Simulate a time-consuming task
    return x * x  # Example computation

def worker(thread_id, value):
    """Thread worker function to perform expensive computation."""
    print(f"Thread {thread_id} starting computation for value: {value}")
    result = expensive_computation(value)
    print(f"Thread {thread_id} got result: {result}")

if __name__ == "__main__":
    threads = []
    values_to_compute = [10, 20, 10, 30, 20, 40]  # Some values are repeated to test caching

    for i, value in enumerate(values_to_compute):
        thread = threading.Thread(target=worker, args=(i+1, value))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All computations are complete.")
    
    print(f"Cache Info: {expensive_computation.cache_info()}")
    clear_cache = input("Do you want to clear the cache? (y/n): ")
    if clear_cache.lower() == 'y':
        expensive_computation.cache_clear()
        print("Cache cleared.")
# ============================================================================