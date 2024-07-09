# Python Async Comprehension

## Description
This project demonstrates the use of asynchronous generators, async comprehensions, and parallel execution using `asyncio` in Python 3.7.

## Files
- `0-async_generator.py`: Defines an asynchronous generator that yields random numbers.
- `1-async_comprehension.py`: Uses an async comprehension to collect random numbers from the async generator.
- `2-measure_runtime.py`: Measures the runtime of running the async comprehension four times in parallel.

## Usage
To run the examples, ensure you have Python 3.7 installed and execute the scripts:

```sh
chmod +x 0-main.py 1-main.py 2-main.py
./0-main.py
./1-main.py
./2-main.py

