# import unittest
#
# # 使用TestCase
# from login import get_username, get_password
#
#
# class TestLogin(unittest.TestCase):
#     def test_login_username(self):
#         # 预期结果：登录自己的账号
#         expect_username = "1"
#         # 实际结果：显示在页面上的账号
#         actual_name = get_username()
#         self.assertEqual(actual_name, expect_username)
#         # assert expect_username == actual_name
#
#     def test_login_password(self):
#         # 预期结果：
#         expect_password = "1008611"
#         # 实际结果：
#         actual_password = get_password()
#         self.assertEqual(actual_password, expect_password)
#         # assert expect_password == actual_password
#
#
# # unittest.main()
#
# # 1.通过TestSuite中的addTest去添加测试用例
#
# # 创建一个测试用例套件，套件可以理解为一组用例的组合
# # suite = unittest.TestSuite()
#
# # 添加一条测试用例：addTest
# # suite.addTest(TestLogin('test_login_username'))
# # suite.addTest(TestLogin('test_login_password'))
#
# # 添加多条测试用例：addTests
# # lst = [TestLogin('test_login_username'), TestLogin('test_login_password')]
# # suite.addTests(lst)
#
#
# # 2.使用TestLoader中的discover来执行测试用例
# suite = unittest.TestLoader().discover('.', pattern='test*.py')
#
# runner = unittest.TextTestRunner()
# runner.run(suite)
