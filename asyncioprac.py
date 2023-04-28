import asyncio



async def test():
    print("Hello this is test function")
    await asyncio.sleep(1)
    print("test 2.5 sec over")
    
async def add(a,b):
    task = asyncio.create_task(test())
    print(f"Value of a is {a}")
    await asyncio.sleep(2)
    print(f"Value of b is {b}")
    print(f"Value of a+b is {a+b}")
    await task 

async def perform():
    task = asyncio.create_task(add(1,4))
    print("hello")
    print(f"The operation being performed is add")
    await asyncio.sleep(0.5)
    print(f"The last print statement - return value")
    await task
    
    
try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

loop.run_until_complete(perform())
loop.close()
