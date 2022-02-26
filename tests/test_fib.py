"""

    # Fibonacci sequence testing and benchmarking the results

"""
from src.fib import fib, mem_fib, dp_fib
import pytest


@pytest.mark.parametrize('data', [10, 50, 100, 150, 250, 350])
def test_fib_1(benchmark, data):
    results = benchmark(fib, data)
    assert results


@pytest.mark.parametrize('data', [10, 50, 100, 150, 250, 350])
def test_fib_2(benchmark, data):
    results = benchmark(mem_fib, data)
    assert results


@pytest.mark.parametrize('data', [10, 50, 100, 150, 250, 350])
def test_fib_3(benchmark, data):
    results = benchmark(dp_fib, data)
    assert results
