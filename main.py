import random
import string
import time
import traceback

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Base:
	def __init__(self):
		options = Options()
		options.add_argument('--start-maximized')
		self.driver = webdriver.Chrome(options=options)

	def go_page(self, url):
		self.driver.get(url)

	def get_element(self, action, script):
		"""
		Hàm lấy elemnt
		:param action: String - Check lấy element theo kiểu nào
		:param script
		:return:
		"""
		if action == 1:
			wait = WebDriverWait(self.driver, 15)
			element = wait.until(EC.presence_of_element_located(script))

		else:
			# element = self.driver.find_element(script)
			wait = WebDriverWait(self.driver, 15)
			element = wait.until(EC.presence_of_all_elements_located(script))
		return element

	###########################################
	def click(self, script):
		element = self.get_element(1, script).click()
		time.sleep(1)
		return element

	def sendkey(self, script, value):
		element = self.get_element(1, script).send_keys(value)
		time.sleep(1)
		return element

	def click_sendkey(self, script, value):
		element = self.get_element(1, script)
		element.click()
		time.sleep(1)
		element.send_keys(value)
		time.sleep(1)


#############################################

class Website1(Base):
	def __init__(self):
		super().__init__()

	def ThayAvata(self, upload):
		element = self.get_element(1, (By.ID, "avatar-upload"))
		element.send_keys(upload)
		time.sleep(2)

	@staticmethod
	def random_string(action):
		"""
		Random ra tài khoản, gmail
		:param action: String - Param check để lấy loại cần lấy
		:return:
		"""
		user = ''
		for idx in range(8):
			x = random.choices(string.ascii_lowercase)
			user += x[0]
		if action == "account":
			return user
		else:
			y = "@gmail.com"
			gmail = user + y
			return gmail

	def website(self):
		self.go_page('https://www.webtretho.com')


	def click_Register(self):
		self.click((By.XPATH, "//*[@class='am-navbar-right ml__20']/a[3]"))
		self.click((By.XPATH, "//*[@class='btn-default btn-primary w-100']"))
		time.sleep(3)

		global str_gmail
		self.sendkey((By.XPATH, "//*[@name='fullName']"), "Lê Văn Tèo")
		str_account = self.random_string("account")

		self.sendkey((By.XPATH, "//*[@id='username']"),str_account)
		self.sendkey((By.XPATH, "//*[@name ='password']"), "THT123456")
		str_gmail = self.random_string("gmail")
		self.sendkey((By.XPATH, "//*[@id='input-email']"),str_gmail)

		# điền vào ngày sinh
		self.click_sendkey((By.XPATH, "//*[@id='rc_select_0']"), "12")
		self.sendkey((By.XPATH, "//*[@id='rc_select_0']"), Keys.ENTER)

		# điền vào tháng sinh

		self.click_sendkey((By.XPATH, "//*[@id='rc_select_1']"), "12")
		self.sendkey((By.XPATH, "//*[@id='rc_select_1']"), Keys.ENTER)

		# Điền vào năm sinh
		self.click_sendkey((By.XPATH, "//*[@id='rc_select_2']"), "1996")
		self.sendkey((By.XPATH, "//*[@id='rc_select_2']"), Keys.ENTER)

		# Click vào hoàn thành đăng ký
		self.click((By.XPATH, "//*[@class='am-list-body']//button"))

	def click_Logout(self):
		self.click((By.XPATH, "//*[@class='navigation-user__arrow']"))
		self.click((By.XPATH, "//div[12][@class='am-list nav-item']"))

	def click_Login(self):
		self.click((By.XPATH, "//*[@class='am-navbar-right ml__20']/a[3]"))
		self.click((By.XPATH, "//*[@class='mx__10 mb__10 w-100']/button"))
# Nhập vào tài khoản
		global str_gmail
		self.sendkey((By.XPATH, "//*[@name ='login']"), str_gmail)
		# self.sendkey((By.XPATH, "//*[@name ='login']"), "lothivisong")
		self.sendkey((By.XPATH, "//*[@name ='password']"), "THT123456")
		# self.sendkey((By.XPATH, "//*[@name ='password']"), "lovisong")
		self.click((By.XPATH, "//button[@class='btn-round btn-login font-size__14 text-bold px__25']"))

	# Truy cập vào trang cá nhân
		self.click((By.XPATH, "//*[@class='navigation-user__arrow']"))
		self.click((By.XPATH, "//*[@class ='am-badge w-100']"))
	# cập nhật ảnh đại diện
		self.ThayAvata(r'C:\Users\DELL\Desktop\2\hoa.jpg')
		time.sleep(3)

	# Xác nhận tài khoản
	def choose_zone(self):
		try:
			self.get_element(1, (By.CSS_SELECTOR, ".issue-by-selection")).click()
			verical_ordinate = 0
			flag_element = False
			element_scroll = self.get_element(1, (By.CSS_SELECTOR, ".rc-virtual-list-holder"))
			print(element_scroll)
			element_all = []

			for i in range(0, 10):
				self.driver.execute_script("arguments[0].scrollTop = arguments[1]", element_scroll, verical_ordinate)
				element_zone = self.get_element(2, (By.XPATH, "//*[@class='ant-select-item-option-content']"))
				for element in element_zone:
					text_zone = element.text
					if text_zone in element_all:
						continue
					else:
						element_all.append(text_zone)
					if 'Hà Nội' == element.text:
						element.click()
						flag_element = True
						break
				if flag_element:
					break
				verical_ordinate += 100
				time.sleep(2)
		except:
			print("choose_zone=============", traceback.format_exc())

		# xác nhận giới tính
		self.click((By.XPATH, "//input[@value='true']"))
		# Điền thông tin chứng minh thư

		self.sendkey((By.XPATH, "//*[@name='identificationNumber']"), "122334556343")
		# Điền vào thông tin ngày cấp
		self.sendkey((By.XPATH, '//*[@placeholder="Ngày cấp"]'), "23/05/2022")
		self.sendkey((By.XPATH, '//*[@placeholder="Ngày cấp"]'), Keys.ENTER)

		# Nhập lại địa chỉ để xác nhận
		self.click_sendkey((By.XPATH, "//*[@name ='address']"), "Hà Nội")

		self.click_sendkey((By.XPATH, "//*[@id='rc_select_0']"), "Hà Nội")
		self.sendkey((By.XPATH, "//*[@id='rc_select_0']"), Keys.ENTER)
		# Nhập vào quận

		self.click_sendkey((By.XPATH, "//*[@id='rc_select_1']"), "Hoàng Mai")
		self.sendkey((By.XPATH, "//*[@id='rc_select_1']"), Keys.ENTER)

		# Nhập vào phường
		self.click_sendkey((By.XPATH, "//*[@id='rc_select_2']"), "Trần Phú")
		self.sendkey((By.XPATH, "//*[@id='rc_select_2']"), Keys.ENTER)

		# Nhập vào sdt

		self.click_sendkey((By.XPATH, "//*[@name='phoneNumber']"), "0977468227")

		# Xác nhận hoàn thành đăng ký
		self.get_element(1, (By.XPATH, "//*[@class='am-list-body']//button")).click()

	def register(self):
		self.website()
		self.click_Register()
		self.click_Logout()
		self.click_Login()
		self.choose_zone()
	def multi_register(self):
		# lay danh sach accc
		for i in []:
			self.register(i)




