# YouTube Comment Scraper

`YouTubeCommentScraper` is a Python package designed to scrape comments from YouTube videos using Selenium. The scraper is customizable, allowing you to run the browser in headless mode, control the timeout, pause time for scrolling, and more. You can also choose whether to log actions and return the page source along with the comments.

## Features

- **Headless Mode**: Run the browser in headless mode (optional).
- **Customizable Timeouts**: Set the timeout for waiting for elements to load.
- **Automatic Scrolling**: Automatically scrolls the page until all comments are loaded.
- **Logging Support**: Enable logging to a file for tracking activities.
- **Return Page Source**: Optionally return the page source along with the comments.
- **BeautifulSoup Integration**: Extract comments using BeautifulSoup for robust parsing.

## Installation

To install the package, use the following command:

```bash
pip install youtube-comments-scrapper
```

## Dependencies

This package requires the following dependencies:

- selenium
- webdriver-manager
- beautifulsoup4
- lxml (optional but recommended for faster HTML parsing)

You can install these dependencies using the following command (optional):

```bash
pip install selenium webdriver-manager beautifulsoup4 lxml
```

## Usage

### 1. Basic Usage: Scraping Comments

Here's a simple example to scrape comments from a YouTube video:

```python
from youtube_comments_scraper import YouTubeCommentScraper

scraper = YouTubeCommentScraper(headless=True, timeout=10, scroll_pause_time=1.5, enable_logging=False, return_page_source=False)
video_url = "https://www.youtube.com/watch?v=Ycg48pVp3SU"
comments = scraper.scrape_comments(video_url)

print("Comments:", comments)
```

### 2. Scraping Comments with Logging Enabled

Enable logging to track the actions performed during scraping:

```python
from youtube_comments_scraper import YouTubeCommentScraper

scraper = YouTubeCommentScraper(headless=True, timeout=10, scroll_pause_time=1.5, enable_logging=True, return_page_source=False)
video_url = "https://www.youtube.com/watch?v=Ycg48pVp3SU"
comments = scraper.scrape_comments(video_url)

print("Comments:", comments)
```

This will generate a log file (youtube_scraper.log) in the current directory.

### 3. Returning Page Source Along with Comments

If you want to extract comments and return the page's HTML source:

```python
from youtube_comments_scraper import YouTubeCommentScraper

scraper = YouTubeCommentScraper(headless=True, timeout=10, scroll_pause_time=1.5, enable_logging=False, return_page_source=True)
video_url = "https://www.youtube.com/watch?v=Ycg48pVp3SU"
comments, page_source = scraper.scrape_comments(video_url)

print("Comments:", comments)
print("Page Source:", page_source)
```

### 4. Custom Scroll Pause Time

You can control how long the scraper pauses between scroll actions using the `scroll_pause_time` parameter:

```python
from youtube_comments_scraper import YouTubeCommentScraper

scraper = YouTubeCommentScraper(headless=True, timeout=10, scroll_pause_time=2.0, enable_logging=False, return_page_source=False)
video_url = "https://www.youtube.com/watch?v=Ycg48pVp3SU"
comments = scraper.scrape_comments(video_url)

print("Comments:", comments)
```


### 5. Scraping Comments Without Scrolling

If you only want to scrape the comments that load without scrolling:

```python
from youtube_comments_scraper import YouTubeCommentScraper

scraper = YouTubeCommentScraper(headless=True, timeout=10, scroll_pause_time=1.5, enable_logging=False, return_page_source=False)
video_url = "https://www.youtube.com/watch?v=Ycg48pVp3SU"
comments = scraper.scrape_comments(video_url, scroll=False)

print("Comments:", comments)
```

### 6. Logging Custom Messages

You can log custom messages using the built-in log_info, log_warning, and log_error methods:

```python
scraper.log_info("This is an info log message.")
scraper.log_warning("This is a warning message.")
scraper.log_error("This is an error message.")
```

## Class Reference

### `YouTubeCommentScraper`

#### `__init__(self, headless=True, timeout=10, scroll_pause_time=1.5, enable_logging=False, return_page_source=False)`

- `headless` (bool): Run the browser in headless mode. Default is `True`.
- `timeout` (int): The maximum time to wait for elements to load. Default is `10` seconds.
- `scroll_pause_time` (float): The pause time between scroll actions. Default is `1.5` seconds.
- `enable_logging` (bool): Whether to enable logging to a file. Default is `False`.
- `return_page_source` (bool): Whether to return the page source along with comments. Default is `False`.

#### `scrape_comments(self, video_url, scroll=True)`

- `video_url` (str): The URL of the YouTube video.
- `scroll` (bool): Whether to scroll the page to load all comments. Default is `True`.

**Returns:**

- A tuple `(comments, page_source)` if `return_page_source` is `True`, otherwise just the list of `comments`.

#### `log_info(self, message)`

- Logs an informational message.

#### `log_warning(self, message)`

- Logs a warning message.

#### `log_error(self, message)`

- Logs an error message.



## License
This project is licensed under the MIT License.




