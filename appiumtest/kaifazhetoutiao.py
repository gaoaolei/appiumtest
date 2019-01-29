from appium import webdriver
import time
desired_caps = {'platformName': 'Android',
                'platformVersion': '7',
                'deviceName': 'samsung galaxy S7',
                'app': r'E:\io.manong.developerdaily_17112812.apk',
                'appPackage': 'io.manong.developerdaily',
                'appActivity': 'io.toutiao.android.ui.activity.LaunchActivity',
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                'noReset': True,
                'newCommandTimeout': 6000
                }
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(1)
code = 'new UiSelector().resourceId("io.manong.developerdaily:id/tab_bar").' \
       'childSelector(new UiSelector().className("android.widget.TextView").instance(3))'
ele = driver.find_element_by_android_uiautomator(code)
print(ele.text)
ele.click()
time.sleep(1)
code2 = 'new UiSelector().textContains("我的")'
eles2 = driver.find_elements_by_android_uiautomator(code2)
for ele2 in eles2:
    print(ele2.text)
# for i in range(5):
#     driver.swipe(700, 1800, 700, 1000, 500)
#     time.sleep(1)
#     driver.swipe(700, 1000, 700, 1800, 500)
#     time.sleep(1)
# 动态获取坐标，克服屏幕分辨率带来的问题，提升代码健壮性
ele = driver.find_element_by_class_name('android.widget.LinearLayout')  # 找到一大块相关区域
time.sleep(1)
location = ele.location       # 左上角坐标
size = ele.size
print(location, size)
x1 = location['x'] + int(size['width']*0.5)
x2 = location['x'] + int(size['width']*0.5)                     # 为什么是字典
y1 = location['y'] + int(size['height']*0.2)
y2 = location['y'] + int(size['height']*0.5)
for i in range(5):
    driver.swipe(x1, y1, x2, y2, 500)
    time.sleep(1)
    driver.swipe(x1, y2, x2, y1, 500)
    time.sleep(1)


