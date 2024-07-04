from fibonacci_tests.fibonacci import FibonacciTest


def entrypoint() -> None:
    
    fibonacci_test = FibonacciTest()

    fibonacci_test.test_fibonacci()
