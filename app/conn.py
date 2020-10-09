from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = 'emulator-5554'
# desired_caps['appPackage'] = 'com.android.calendar'
# desired_caps['appActivity'] = 'com.android.calendar.AllInOneActivity'
desired_caps['browserName'] = 'Chrome'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.find_element_by_name('4').click()
# # driver.find_element_by_name('+').click()
# # driver.find_element_by_name('4').click()
# # driver.find_element_by_name('=').click()
driver.get('http://www.baidu.com')