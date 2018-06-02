# coding=utf-8

from utilities.core import *


class Baidu(Core):
    def test1_title(self):
        """检查title"""
        e=EC.title_is('百度一下，你就知道')
        self.assertTrue(e(self.dr))

    def test2_news(self):
        """检查news"""
        e=EC.visibility_of_element_located(('name','tj_trnews'))
        self.assertTrue(e(self.dr))

    def test3_hao123(self):
        """检查hao123"""
        e=EC.text_to_be_present_in_element(('name','tj_trhao123'),'hao123')
        self.assertTrue(e(self.dr))

    def test4_value(self):
        """检查8对应元素的value中 """
        e=EC.text_to_be_present_in_element_value(('xpath',
            '//input[@name="f"]'),'8')
        self.assertTrue(e(self.dr))



    def test6(self):
        """使用WebDriverWait"""
        self.assertTrue(False)
        e=self.dr.find_element_by_link_text('设置')
        ActionChains(self.dr).move_to_element(e).perform()

        # e=WebDriverWait(self.dr,10,0.5).until(
        #     EC.presence_of_element_located(('link text','搜索历史'))
        #     )
        # e.click()

        WebDriverWait(self.dr,10,0.5).until(
                lambda driver:driver.find_element_by_link_text("搜索历史").is_displayed())
        self.dr.find_element_by_link_text('搜索历史').click()



if __name__=='__main__':
    # suite=unittest.TestSuite()
    # suite.addTest(Baidu('test2'))
    # suite.addTest(Baidu('test1'))

    # runner=unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main()


