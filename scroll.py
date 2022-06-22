import pytest
import sys

@pytest.mark.usefixtures('driver')
class TestLink:
	def scroll_bottom():
		"""
		Verify scrolling to bottom
		:return: None
		"""
		driver.get('https://www.lambdatest.com/')
		driver.maximize_window()
		sleep(2)
		success = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		sleep(5)
		assert success == True
	
	def scroll_infinite():
		"""
		Verify infinite scroll
		:return: None
		"""
		SCROLL_PAUSE_TIME = 0.5

		# Get scroll height
		last_height = driver.execute_script("return document.body.scrollHeight")

		#controls how many times scrolled to bottom
		scroll_pass = 0

		#change to True for infinite scroll
		while scroll_pass < 10:
			# Scroll down to bottom
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

			# Wait to load page
			time.sleep(SCROLL_PAUSE_TIME)

			# Calculate new scroll height and compare with last scroll height
			new_height = driver.execute_script("return document.body.scrollHeight")
			if new_height == last_height:
				break
			last_height = new_height
			scroll_pass+=1
	
