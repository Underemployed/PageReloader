from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def manage_tabs(url, num_tabs=3, interval=5):
    driver = webdriver.Chrome()
    
    # Open desired number of tabs
    for _ in range(num_tabs):
        driver.execute_script("window.open('');")
    
    # Get all window handles
    tabs = driver.window_handles
    
    # Load URL in each tab
    for i, tab in enumerate(tabs):
        driver.switch_to.window(tab)
        driver.get(url)
        print(f"Loaded tab {i+1}")
    
    try:
        while True:
            for tab in tabs:
                driver.switch_to.window(tab)
                driver.refresh()
                print(f"Reloaded tab {tabs.index(tab)+1}")
            time.sleep(interval)

    except KeyboardInterrupt:
        driver.quit()

# Example usage
url = "https://example.com"
manage_tabs(url, num_tabs=20, interval=5)
