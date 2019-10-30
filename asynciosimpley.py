import asyncio
async def nested():
    print(42)
    return 42

async def main():
    task = asyncio.create_task(nested())

    await task

asyncio.run(main())