# grabbing CAPTCHA

from PIL import Image
import urllib
from selenium import webdriver

def get_captcha(driver, element, path):
    location = element.location
    size = element.size
    driver.save_screenshot(path)
    image = Image.open(path)

    left = location['x']
    top = location['y'] 
    right = location['x'] + size['width']
    bottom = location['y'] + size['height'] 
    
    image = image.crop((left, top, right, bottom))  # defines crop points
    image.save(path, 'jpeg')  # saves new cropped image

for i in range(1, 201):
    driver = webdriver.PhantomJS()
    driver.get('http://www.freelibros.org/wp-login.php')
    img = driver.find_element_by_xpath('html/body/div[1]/form/p[3]/label/img')
    get_captcha(driver, img, "testcaptcha/" + str(i) + ".jpeg")
    driver.close()


