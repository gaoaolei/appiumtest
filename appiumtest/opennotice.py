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
driver.open_notifications()
time.sleep(2)
driver.press_keycode(4)
