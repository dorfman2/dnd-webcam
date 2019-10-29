import asyncio
import random
import time

async def servo(name, queue):
    while True:
        # Get a "work item" out of the queue.
        sleep_for = await queue.get()

        # Sleep for the "sleep_for" seconds.
        await asyncio.sleep(sleep_for)

        # Notify the queue that the "work item" is complete.
        queue.task_done()

        print(f'{name} has slept for {sleep_for:.2f} seconds')

async def main():
    # Create a queue that we will use to store our "workload".
    queue = asyncio.Queue()

    # Generate random timings and put them into a queue.
    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.randint(1, 4)
        total_sleep_time += sleep_for
        queue.put_nowait(sleep_for)

    # Create 3 servo tasks to process the queue concurrently.
    tasks = []
    for i in range(3):
        task = asyncio.create_task(servo(f'servo-{i}', queue))
        tasks.append(task)

    # Wait until the queue is fully processed.
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    # Cancel our servo tasks.
    for task in tasks:
        task.cancel()

    print('====')
    print(f'3 Workers moved in parallel for {total_slept_for:.2f} seconds')
    print(f'total expected sleep time: {total_sleep_time:.2f} seconds')

asyncio.run(main())