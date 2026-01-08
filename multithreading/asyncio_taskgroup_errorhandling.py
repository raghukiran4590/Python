import asyncio
import traceback

async def faulty_task(name, delay):
    await asyncio.sleep(delay)
    if name == 'task_b':
        raise ValueError(f"{name} failed!")
    return f"{name} completed"

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(faulty_task('task_a', 2))
            tg.create_task(faulty_task('task_b', 1))
            tg.create_task(faulty_task('task_c', 3))

        # raise ExceptionGroup("Multiple problems", [ValueError("Bad value"), TypeError("Wrong type")])
    except* TypeError as e_type:
        print(f"Caught a TypeError exception group:")
        for exc in e_type.exceptions:
            print(f"- {exc}")

    except* ValueError as eg:
        print(f"Caught a ValueError exception group:")
        for exc in eg.exceptions:
            print(f"- {exc}")


if __name__ == "__main__":
    asyncio.run(main())
