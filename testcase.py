# -*- coding:utf8 -*-
''' Create on "2017/10/13 16:23"
    _author_="zhao ling"
    Poject: 测试用例层
    测试数据：
        2,3
    先简单实现测试数据的输入
 '''

import unittest
from num import number

class testnumber(unittest.TestCase):
    # 先来一个不从数据库或excel取数的
    def setUp(self):
        self.n = number(2,3)

    def tearDown(self):
        print('tear down.')

    def test_noNone(self):
        self.assertEqual(2,0,msg='a is not equal 0')
        self.assertEqual(self.b,0,msg='b is not equal 0')

    def test_add(self):
        self.assertEqual(self.n.add(),5,msg='add is error')

if __name__ == '__main__':
    unittest.main()