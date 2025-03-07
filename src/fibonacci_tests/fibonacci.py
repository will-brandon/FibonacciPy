"""
File:   fibonacci_tests/fibonacci.py
Type:   Python Test Module
Author: Will Brandon <dev.willbrandon, gmail.com>
Date:   Thu, Jul 4, 2024

Copyright (c) Will Brandon, 2024.

Tests fibonacci/fibonacci.py.
"""

from juntest.test_base import TestBase

from fibonacci.fibonacci import fibonacci


class FibonacciTest(TestBase):

    def test_fibonacci(self) -> None:

        self.assert_except(fibonacci, ValueError, -1)

        self.assert_equal(fibonacci(0),  [])
        self.assert_equal(fibonacci(1),  [1])
        self.assert_equal(fibonacci(2),  [1, 1])
        self.assert_equal(fibonacci(3),  [1, 1, 2])
        self.assert_equal(fibonacci(4),  [1, 1, 2, 3])
        self.assert_equal(fibonacci(5),  [1, 1, 2, 3, 5])
        self.assert_equal(fibonacci(6),  [1, 1, 2, 3, 5, 8])
        self.assert_equal(fibonacci(7),  [1, 1, 2, 3, 5, 8, 13])
        self.assert_equal(fibonacci(20), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
                                          4181, 6765])
        self.assert_equal(fibonacci(40), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
                                          4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
                                          832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
                                          39088169, 63245986, 102334155])
        self.assert_equal(fibonacci(90), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
                                          4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
                                          832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
                                          39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733,
                                          1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025,
                                          20365011074, 32951280099, 53316291173, 86267571272, 139583862445,
                                          225851433717, 365435296162, 591286729879, 956722026041, 1548008755920,
                                          2504730781961, 4052739537881, 6557470319842, 10610209857723, 17167680177565,
                                          27777890035288, 44945570212853, 72723460248141, 117669030460994,
                                          190392490709135, 308061521170129, 498454011879264, 806515533049393,
                                          1304969544928657, 2111485077978050, 3416454622906707, 5527939700884757,
                                          8944394323791464, 14472334024676221, 23416728348467685, 37889062373143906,
                                          61305790721611591, 99194853094755497, 160500643816367088, 259695496911122585,
                                          420196140727489673, 679891637638612258, 1100087778366101931,
                                          1779979416004714189, 2880067194370816120])
        self.assert_equal(fibonacci(93), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
                                          4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
                                          832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
                                          39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733,
                                          1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025,
                                          20365011074, 32951280099, 53316291173, 86267571272, 139583862445,
                                          225851433717, 365435296162, 591286729879, 956722026041, 1548008755920,
                                          2504730781961, 4052739537881, 6557470319842, 10610209857723, 17167680177565,
                                          27777890035288, 44945570212853, 72723460248141, 117669030460994,
                                          190392490709135, 308061521170129, 498454011879264, 806515533049393,
                                          1304969544928657, 2111485077978050, 3416454622906707, 5527939700884757,
                                          8944394323791464, 14472334024676221, 23416728348467685, 37889062373143906,
                                          61305790721611591, 99194853094755497, 160500643816367088, 259695496911122585,
                                          420196140727489673, 679891637638612258, 1100087778366101931,
                                          1779979416004714189, 2880067194370816120, 4660046610375530309,
                                          7540113804746346429, 12200160415121876738])
