import asyncio

async def might_fail(name):
    try:
        print(f"Task {name} starting...")
        await asyncio.sleep(1)
        if name == "task_b":
            raise ValueError(f"{name} failed!")
        print(f"Task {name} finished successfully.")
    except ValueError as e:
        print(f"Handled error in {name}: {e}")
    # Other exceptions can be handled or ignored as needed

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(might_fail("task_a"))
        tg.create_task(might_fail("task_b"))
        tg.create_task(might_fail("task_c"))
    
    print("All tasks completed or exceptions handled.")

if __name__ == "__main__":
    asyncio.run(main())
