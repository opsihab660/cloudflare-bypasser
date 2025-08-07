from CloudflareBypasser import CloudflareBypasser
from DrissionPage import ChromiumPage, ChromiumOptions

def main():
    # Configure the browser for headless mode
    co = ChromiumOptions()
    co.set_argument('--headless')
    co.set_argument('--no-sandbox')

    # Initialize the browser with the options
    driver = ChromiumPage(addr_or_opts=co)
    
    # Navigate to the target page
    driver.get('https://mediateluk.com/sms/index.php?login=1')
    
    # Create a CloudflareBypasser instance and run the bypass
    cf_bypasser = CloudflareBypasser(driver)
    cf_bypasser.bypass()
    
    # Keep the script running if needed, or add other logic here
    print("Cloudflare bypass attempt finished.")
    driver.quit()

if __name__ == "__main__":
    main()