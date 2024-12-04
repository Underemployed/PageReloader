from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def manage_tabs(url, num_tabs=20, interval=5, iterations=1000):
    chrome_options = Options()
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get(url)
    for _ in range(num_tabs - 1):
        driver.execute_script("window.open(arguments[0])", url)
    
    tabs = driver.window_handles
    count = 0
    
    try:
        while count < iterations:
            # Reload all tabs at once
            for tab in tabs:
                driver.switch_to.window(tab)
                driver.refresh()
            count += 1
            print(f"Iteration {count}/{iterations} - Reloaded all {num_tabs} tabs")
            time.sleep(interval)
            
        print(f"Completed {iterations} iterations across {num_tabs} tabs!")
        driver.quit()
    except KeyboardInterrupt:
        driver.quit()

url = "https://example.com"
manage_tabs(url, num_tabs=20, interval=5, iterations=1000)
