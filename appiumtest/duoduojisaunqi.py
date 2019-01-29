from appium import webdriver
import time
desired_caps = {
                'platformName': 'Android',
                'platformVersion': '7',
                'deviceName': 'samsung Galaxy S7',
                'app': 'E:/ddjsq.apk',
                'appPackage': 'com.ibox.calculators',
                'appActivity': 'com.qihoo.util.StartActivity',
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                'noReset': True,
                'newCommandTimeout': 6000
                }
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.implicitly_wait(10)
driver.find_element_by_id('com.ibox.calculators:id/update_id_cancel').click()
time.sleep(10)
digit3 = driver.find_element_by_id('com.ibox.calculators:id/digit3')
digit9 = driver.find_element_by_id('com.ibox.calculators:id/digit9')
digit5 = driver.find_element_by_id('com.ibox.calculators:id/digit5')
plus = driver.find_element_by_id('com.ibox.calculators:id/plus')
equal = driver.find_element_by_id('com.ibox.calculators:id/equal')
mul = driver.find_element_by_id('com.ibox.calculators:id/mul')

time.sleep(1)

digit3.click()
plus.click()
digit9.click()
equal.click()
mul.click()
digit5.clcick()
equal.click()