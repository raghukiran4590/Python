import asyncio

async def function1():
    print('function-1')

async def function2():
    print('function-2')

async def function3():
    print('function-3')

if __name__ == "__main__":
    asyncio.run(function1())
    asyncio.run(function2())
    asyncio.run(function3())



