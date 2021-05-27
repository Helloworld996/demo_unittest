import unittest

# 使用TestCase
from login import get_username, get_password

version = 3.0


class TestLogin(unittest.TestCase):
    # 类的初始化方法
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass:执行类之前调用一次")

    # 类的清空方法
    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass:执行类之后调用一次")

    # 初始化方法
    def setUp(self) -> None:
        print("setUp:执行测试用例前")

    # 清空方法
    def tearDown(self) -> None:
        print("tearDown:执行测试用例后")

    def test_login_username(self):
        print("获取用户名执行测试用例")
        # 预期结果：登录自己的账号
        expect_username = "1"
        # 实际结果：显示在页面上的账号
        actual_name = get_username()
        self.assertEqual(actual_name, expect_username)
        # assert expect_username == actual_name

    # @unittest.skipIf(version > 2.0, "跳过测试用例")
    def test_login_password(self):
        print("获取密码执行测试用例")
        # 预期结果：
        expect_password = "1008611"
        # 实际结果：
        actual_password = get_password()
        self.assertEqual(actual_password, expect_password)
        # assert expect_password == actual_password


# unittest.main()

# 1.通过TestSuite中的addTest去添加测试用例

# 创建一个测试用例套件，套件可以理解为一组用例的组合
suite = unittest.TestSuite()

# 添加一条测试用例：addTest
suite.addTest(TestLogin('test_login_username'))
suite.addTest(TestLogin('test_login_password'))

# 添加多条测试用例：addTests
# lst = [TestLogin('test_login_username'), TestLogin('test_login_password')]
# suite.addTests(lst)


# 2.使用TestLoader中的discover来执行测试用例
# suite = unittest.TestLoader().discover('.', pattern='test*.py')

runner = unittest.TextTestRunner()
runner.run(suite)
