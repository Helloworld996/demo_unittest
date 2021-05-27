import unittest


# 实现加法的方法

def add(x, y):
    return x + y


class TestAdd(unittest.TestCase):
    # def test_add_01(self):
    #     res1 = add(1, 2)
    #     self.assertEqual(3, res1)
    #
    # def test_add_02(self):
    #     res2 = add(2, 0)
    #     self.assertEqual(2, res2)
    #
    # def test_add_03(self):
    #     res3 = add(-2, 2)
    #     self.assertEqual(0, res3)

    def test_add(self):
        test_data = [(1, 2, 3), (2, 0, 2), (-2, 2, 0)]
        for x, y, expect_value in test_data:
            res = add(x, y)
            self.assertEqual(expect_value, res)


if __name__ == '__main__':
    unittest.main()
# suite = unittest.TestSuite()
# suite.addTest(TestAdd('test_add_01'))
# suite.addTest(TestAdd('test_add_02'))
# suite.addTest(TestAdd('test_add_03'))
#
# # suite = unittest.TestLoader().discover('.', pattern='test*.py')
#
# runner = unittest.TextTestRunner()
# runner.run(suite)
