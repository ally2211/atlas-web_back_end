## Python - Async Comprehension
### 1. **How to Write an Asynchronous Generator**

An asynchronous generator is similar to a regular generator, but it allows you to `await` asynchronous operations within the generator's body. You define an asynchronous generator using `async def` and use `yield` to produce values, just like in a normal generator. You can use `await` inside the generator to perform asynchronous tasks.

**Example:**

```python
import asyncio

async def async_gen():
    for i in range(5):
        await asyncio.sleep(1)  # Simulate an asynchronous operation
        yield i  # Produce the value

# Usage of async generator
async def main():
    async for value in async_gen():  # Asynchronously iterate over the generator
        print(value)

asyncio.run(main())
```

**Explanation:**
- **`async def`:** The generator function is defined as asynchronous using `async def`.
- **`yield`:** The generator yields values using the `yield` keyword, just like in a regular generator.
- **`await`:** You can use `await` within the generator to pause the function and wait for the result of an asynchronous operation.

### 2. **How to Use Async Comprehensions**

Async comprehensions are similar to regular comprehensions, but they work with asynchronous iterators (like asynchronous generators). They allow you to concisely process items produced by asynchronous iterators.

**Example:**

```python
import asyncio

async def async_gen():
    for i in range(5):
        await asyncio.sleep(1)
        yield i

async def main():
    result = [x async for x in async_gen()]  # Async comprehension
    print(result)

asyncio.run(main())
```

**Explanation:**
- **`async for`:** Used inside the comprehension to asynchronously iterate over the items produced by the asynchronous generator.
- **Comprehension:** The comprehension `[x async for x in async_gen()]` collects the values yielded by `async_gen()` into a list.

### 3. **How to Type-Annotate Generators**

When type-annotating generators in Python, you need to specify the types of the values that the generator yields, the type of the values sent to the generator, and the type of the value returned by the generator.

For asynchronous generators, you use the `typing.AsyncGenerator` type. This takes two type parameters: the type of values yielded and the type of the value returned when the generator is exhausted (if any).

**Example:**

```python
from typing import AsyncGenerator

async def async_gen() -> AsyncGenerator[int, None]:
    for i in range(5):
        await asyncio.sleep(1)
        yield i
```

**Explanation:**
- **`AsyncGenerator[int, None]`:** This annotation indicates that the generator yields `int` values and does not return any value when it’s done (hence `None`).

For a regular (synchronous) generator, you would use `Generator` from `typing`:

```python
from typing import Generator

def sync_gen() -> Generator[int, None, None]:
    for i in range(5):
        yield i
```

**Explanation:**
- **`Generator[int, None, None]`:** This indicates that the generator yields `int` values, expects `None` for values sent to it (if any), and returns `None` when it completes.

### Summary

- **Asynchronous Generators:** Allow you to yield values from a generator while awaiting asynchronous operations.
- **Async Comprehensions:** Enable you to process items produced by asynchronous iterators in a concise manner.
- **Type-Annotation of Generators:** Specify the types of values yielded, sent, and returned by a generator using `AsyncGenerator` for asynchronous generators and `Generator` for synchronous ones.

### Tasks
- Task 0:  Write a coroutine called async_generator that takes no arguments.  
The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.
- Task 1:  Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.
The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.
- Task 2:  Run time for four parallel comprehensions.
Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
Notice that the total runtime is roughly 10 seconds, explain it to yourself.