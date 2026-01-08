import asyncio

async def might_fail(name):
    await asyncio.sleep(1)
    if name == "task_b":
        raise ValueError(f"{name} failed!")
    return f"{name} success"

async def main_gather():
    tasks = [might_fail("task_a"), might_fail("task_b"), might_fail("task_c")]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    for result in results:
        if isinstance(result, Exception):
            print(f"An exception occurred: {result}")
        else:
            print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main_gather())
