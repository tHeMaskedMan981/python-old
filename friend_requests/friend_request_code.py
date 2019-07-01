import openpyxl,webbrowser,unicodedata, sys, pyperclip,pyautogui,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# enter the name of the file below 
wb = openpyxl.load_workbook('fr.xlsx')
activeSheet = wb.active

# just some constant. helpful for defining mouse behavior
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
i=1
# open command prompt. type python. import pyautogui. then pyautogui.position() after placing ur mouse where 
# option for add friend appears. this will basically give u the cordinates of that point. store them in x 
# and y. the values of x and y for me will be different than for u. 
x=710
y=419
pyautogui.moveTo(x, y, duration=0.1)

browser = webdriver.Chrome()
# browser = webdriver.Firefox()
browser.get('http://facebook.com/')
main_window = browser.current_window_handle

time.sleep(2)
emailElem = browser.find_element_by_id('email')
# enter your email
emailElem.send_keys('')
passwordElem = browser.find_element_by_id('pass')
# enter your password
passwordElem.send_keys('')
passwordElem.submit()
time.sleep(2)

# in the range, just put the range of rows in which links are there which you want to cover. can use 50 per 
# time. ie (1,50), (51,100), etc.
for i in range (51,100):
	# column number with the links. 
	address = activeSheet.cell(row=i, column = 4).value
	
	if address is not None:
	# if (len(profile)!=0):

		profile = address.encode('ascii','ignore')

		print profile
		browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
		browser.get(profile)
		if (i==1):
			i=i+1
			time.sleep(4)

		try:
			element = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "FriendRequestAdd")))
		except Exception as e:
			pass
		# time.sleep(3)
		sources = browser.page_source
		
		source = sources.encode('ascii','ignore')
		print source
		try:
			addfriend = browser.find_element_by_class_name('FriendRequestAdd')
			# addfriend = browser.find_element_by_css_selector('._42ft _4jy.FriendRequestAdd.addButton._4jy4 _517h _9c6')
			print "element found"
			# addfriend = browser.findElement(By.cssSelector('._42ft _4jy.FriendRequestAdd.addButton._4jy4 _517h _9c6'))
			print addfriend
			print "element printed"
			# addfriend1 = browser.find_element_by_id('u_ps_0_0_3')
			# addfriend2 = browser.find_element_by_id('u_0_1a')
			# print addfriend2.text
			try:
				wait = WebDriverWait(browser, 3)
				element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "FriendRequestAdd")))
			except Exception as e:
				pass
			
			addfriend.click()
			print "clicked"
			# addfriend1.click()

		except Exception as e:
			print "nothing found of this type"
			print e
			pass

		# addfriend = browser.find_element_by_class_name('FriendRequestAdd')
		# addfriend.click()
		# pyautogui.click()
		# pyautogui.click(647,438)
		# pyautogui.click()

		time.sleep(1)
		browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')

browser.quit()
print "friend request sending.... done"