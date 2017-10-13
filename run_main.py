# -*- coding:utf8 -*-
''' Create on "2017/10/13 16:23"
    _author_="zhao ling"
    Poject: 输出测试报告
    只能在命令行下 python执行
    ide找不到HTMLTestRunner包
    添加路径也不行的
 '''
import testcase
import unittest
import time,sys
from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':

    suites = unittest.TestSuite()

    suites.addTest(testcase.testnumber('test_add'))
    suites.addTest(testcase.testnumber('test_noNone'))

    #runner = unittest.TextTestRunner()
    #repo = runner.run(suites)

    # set report
    #now = time.strftime('%Y-%m-%d %T_%M_%S')
    now = time.strftime('%Y-%m-%d %H.%M.%S')
    #filename = './report/'+ now + '_result.html'
    filename = now + '_result.html'
    fp = open(filename,'wb')

    repohtml = HTMLTestRunner(stream = fp,title = 'Number test report',
                              description = 'Implementation:')
    repohtml.run(suites)
    fp.close()

