# coding=utf-8

import unittest
import paramunittest


@paramunittest.parametrized(
    (1,1,2),
    (-1,1,0),
    (0,0,0),
    # (('name','tj_trhao123'),'hao123'),
)

class Test(unittest.TestCase):

    def setParameters(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def test(self):
        self.assertEqual(self.a+self.b,self.c)

if __name__=='__main__':
    unittest.main()
