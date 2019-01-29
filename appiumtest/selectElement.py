'''
node detial包含内容
1.index：表示该元素是父元素的第几个节点
2.text：文本内容
3.resource-id：类似于web的id，一般唯一标志
4.class：决定元素类型，类似tag
5.package：包名
6.content-desc：描述信息
7.checkable：可勾选
8.clickable：可点击
9.enabled:
10.focusable:
11.focused:
12.scrollable:
13.long-clickable:
14.bounds：边界坐标
--------------代码-------------
driver.find_element_by_xxx
driver.find_elements_by_xxx
ele.find_element_by_xxx
ele.find_elements_by_xxx
-------------------------------
一、根据ID（resource-id）
    注意：by_id而不是by_resource-id
    有些不严谨的app的id不唯一，我们如何判断id不唯一了？
    答:将界面的文本内容保存到本地，然后ctrl+F搜索id的个数
二、根据calss name（类似于web的tag）
    一般是选择多个，一类的元素
三、根据accessibility_id
    其实就是content-desc
四、根据xpath
    css是web专有的，所以appium没法使用css_selector，但是appium支持xpath来定位元素
    driver.find_element_by_xpath('//ele1/ele2[@attr='a1']')
    xpath不成熟，有bug
    用class做节点  //子元素   /直接子元素   [元素属性]  [n]第几个节点
    ************第三课上最后一部分讲解请试一试
五、使用inspector
    打开inspector的两种方法：
    1.创建新的session
    2.attach到已有的session
    点击搜索按钮----填入desired capabilities-----保存----启动----刷新-----获取界面----定位元素
    inspector的好处：
        1.直接展示了resource-id
        2.可点击跳转并实时跟踪界面
        3.有坐标轴
            click和tap的区别
            click是点击元素，tap是点击坐标
            driver.tap([(120,230)],300)
六、根据uiautomator接口定位元素
1.通过className和text,textContains,textMatches(正则表达式eg:^,$),textStartWith属性
code='new UiSelector().text('我的').className('android.widget.TextView')'       # text和className是且的关系
ele= driver.find_element_by_android_uiautomator(code)
2.根据resource id属性
code='new UiSelector().resourceId('io.manong.developerdaily:id/theid')'
3.根据childSlector和instance方法  类似于xpath     instance从1开始
new UiSelector().resourceId('io.manong.developerdaily:id/tab_bar').childSelector(
    new UiSelector().className('android.widget.TextView').instance(3))
'''

'''
操作元素
click
tap
sendkeys
swipe(start_x,s_y,end_x.e_y,duration) 滑动
scroll(origin_el, destination_el)



获取屏幕尺寸 
screenSize = driver.get_window_size()
w = screenSize['width']
h = screenSize['height']
'''