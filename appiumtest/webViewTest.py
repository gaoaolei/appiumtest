'''
对app中内嵌的web进行自动化时需要开发人员在源代码中进行修改编译，对webview对象加入setWebContentsDebuggingEnabled的调用
protected void onCreate(Bundle saveInstanceState){
    super.onCreate(savedInstanceState);
    WebView myWebView = (WebView) findViewById(R.id.jcywebview);
    myWebView.setWebContentsDebuggingEnabled(true);
    }

webview的自动化
第一种情况：完全不依赖app的web的处理情况
    只是打开一个url
    直接使用chrome打开对应的网页
    使用手机模式

    appium中所有的界面环境称为context
    native（原生部分）的context称为NATIVE_APP
    webview（内嵌web部分）的context称为WEBVIEW_xxx (package name)       （类似于web中frame）
    查看当前有哪些context     driver.contexts
    显示当前context          driver.current_context
    driver.switch_to.context('WEBVIEW_com.qiyi.video')
    driver.switch_to.context(NATIVE_APP)
第二种情况：依赖app的web处理情况
    通过chrome远程调试
    打开chrome浏览器，地址栏输入chrome://inspect
    点击手机样子的小方框
'''

'''
小技巧：
打开通知栏   driver.open_notifications()
按键操作     driver.press_keycode(4)    keycode对应按键查找文档
                                        http://developer..android.com/reference/android/view/KeyEvent.html
       4是返回                                 
'''
