# %%
# firefox起動テスト

# %%
from selenium import webdriver
import time

try:
    url = 'https://www.yahoo.co.jp/'
    # オプション
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver  = webdriver.Firefox(options=options)
    driver.set_page_load_timeout(10)
    driver.set_script_timeout(10)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url)
except Exception as e:
    print(e)
finally:
    time.sleep(3)
    # driver.save_screenshot('Screenshot_test.png')
    driver.quit()
    print('終了しました')

# %%
# driver.quit()

# %%



