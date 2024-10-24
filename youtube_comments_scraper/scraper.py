from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from bs4 import BeautifulSoup
import logging

class YouTubeCommentScraper:
    """
    A class to scrape comments from YouTube videos using Selenium.

    Attributes:
        headless (bool): Whether to run the browser in headless mode.
        timeout (int): The maximum time to wait for elements to load.
        scroll_pause_time (float): The pause time between scroll actions.
        enable_logging (bool): Whether to enable logging to a file.
        return_page_source (bool): Whether to return page source along with comments.
    """

    def __init__(self, headless=True, timeout=10, scroll_pause_time=1.5, 
                 enable_logging=False, return_page_source=False):
        """Initialize the YouTubeCommentScraper with customizable options."""
        self.timeout = timeout
        self.scroll_pause_time = scroll_pause_time
        self.return_page_source = return_page_source
        self.driver = self._init_driver(headless)

        # Configure logging if enabled
        self.enable_logging = enable_logging
        if self.enable_logging:
            logging.basicConfig(
                filename='youtube_scraper.log', 
                level=logging.INFO, 
                format='%(asctime)s - %(levelname)s - %(message)s'
            )
            self.log_info("Logging is enabled.")
        
    def log_info(self, message):
        """Log an info message if logging is enabled."""
        if self.enable_logging:
            logging.info(message)
    
    def log_warning(self, message):
        """Log a warning message if logging is enabled."""
        if self.enable_logging:
            logging.warning(message)
    
    def log_error(self, message):
        """Log an error message if logging is enabled."""
        if self.enable_logging:
            logging.error(message)

    def _init_driver(self, headless):
        """Initialize and return a Chrome WebDriver instance with specified options."""
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    def wait_for_element(self, by, value):
        """Wait for an element to appear within the specified timeout."""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            self.log_warning(f"Element not found: {value}")
            return None

    def scroll_until_all_comments_loaded(self):
        """Scroll down the page until all comments are loaded."""
        last_height = self.driver.execute_script("return document.documentElement.scrollHeight")
        self.log_info("Scrolling to load comments...")

        while True:
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(self.scroll_pause_time)

            new_height = self.driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                self.log_info("All comments loaded.")
                break
            last_height = new_height

    def extract_comments(self):
        """Extract and return top-level comments using BeautifulSoup."""
        page_source = self.get_page_source()
        soup = BeautifulSoup(page_source, 'html.parser')
        comment_elements = soup.select('#content-text')

        comments = [element.get_text(strip=True) for element in comment_elements]
        self.log_info(f"Extracted {len(comments)} comments.")
        return comments

    def get_page_source(self):
        """Return the HTML source of the current page."""
        self.log_info("Fetching page source.")
        return self.driver.page_source

    def scrape_comments(self, video_url, scroll=True):
        """
        Scrape comments from a YouTube video.

        Args:
            video_url (str): The URL of the YouTube video.
            scroll (bool): Whether to scroll the page to load all comments.

        Returns:
            tuple or list: A tuple of comments and page source if return_page_source is True,
                           otherwise just a list of comments.
        """
        try:
            self.log_info(f"Opening URL: {video_url}")
            self.driver.get(video_url)

            # Wait for the comments section to load
            self.wait_for_element(By.TAG_NAME, 'ytd-comments')

            if scroll:
                self.scroll_until_all_comments_loaded()

            comments = self.extract_comments()

            if self.return_page_source:
                page_source = self.get_page_source()
                return comments, page_source

            return comments
        except Exception as e:
            self.log_error(f"An error occurred: {e}")
            return ([], "") if self.return_page_source else []
        finally:
            self.driver.quit()
            self.log_info("Driver closed.")


# Usage example
# scraper = YouTubeCommentScraper(
#     headless=True, 
#     timeout=10, 
#     scroll_pause_time=1.5, 
#     enable_logging=True, 
#     return_page_source=True  # Change to False to return only comments
# )

# # Scrape comments from the provided YouTube video URL
# video_url = "https://www.youtube.com/watch?v=Ycg48pVp3SU&t=7886s"
# result = scraper.scrape_comments(video_url)

# # Print the result based on the return_page_source flag
# if scraper.return_page_source:
#     comments, page_source = result
#     print("Page Source:", page_source)
# else:
#     comments = result

# print("Comments:", comments)
