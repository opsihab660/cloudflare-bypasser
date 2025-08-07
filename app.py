from CloudflareBypasser import CloudflareBypasser
from DrissionPage import ChromiumPage, ChromiumOptions

def main():
    # Configure the browser for resource optimization
    co = ChromiumOptions()
    co.set_argument('--no-sandbox')
    co.set_argument('--disable-dev-shm-usage')
    

    # Initialize the browser with the options
    driver = ChromiumPage(addr_or_opts=co)
    
    # Navigate to the target page
    driver.get('https://nopecha.com/demo/cloudflare')
    
    # Create a CloudflareBypasser instance and run the bypass
    cf_bypasser = CloudflareBypasser(driver)
    cf_bypasser.bypass()
    
    # Keep the script running if needed, or add other logic here
    print("Cloudflare bypass attempt finished.")
    driver.quit()

if __name__ == "__main__":
    main()
