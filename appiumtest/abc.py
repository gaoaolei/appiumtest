'''
1.appium同时只能处理一个session，可勾选allowed session override
2.sdk/tools/bin/uiautomatorviewer.bat查看元素，但是启动时会报错，是该bat的脚本有问题，
    需要将最后一行bindir改成你的tools的路径
3.uiautomatorviewer不能实时跟踪手机界面的变化，需重新获取
'''
from appium import webdriver
import time
desired_caps = {'platformName': 'Android',
                'platformVersion': '7',
                'deviceName': 'samsung galaxy S7',
                'app': r'D:\123platform-tools\PbbReader_V1.6.4.apk',
                'appPackage': 'cn.com.pyc.pbb',
                'appActivity': 'cn.com.pyc.receive.ReceiveActivity',
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                'noReset': True,
                'newCommandTimeout': 6000
                }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.implicitily_wait(10)
driver.find_element_by_id('cn.com.pyc.pbb:id/arl_imv_folder').click()
time.sleep(1)
driver.find_element_by_id('cn.com.pyc.pbb:id/afs_imv_pic').click()
time.sleep(1)
driver.find_element_by_id('cn.com.pyc.pbb:id/afs_txt_name').click()
time.sleep(1)
driver.find_element_by_id('cn.com.pyc.pbb:id/afs_txt_date').click()
time.sleep(1)



# dfadfdfdfdffdafdfsadfa fadfa