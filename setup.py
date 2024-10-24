from setuptools import setup, find_packages

setup(
    name='youtube-comments-scrapper',  # Replace with your package name
    version='1.0.0',
    description='A Python package to scrape YouTube comments using Selenium and BeautifulSoup',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author='Abhishek Kumar',
    author_email='abhiop.dev@gmail.com',
    url='https://github.com/Abhi9868/Youtube-Comment-Scraper',  # Replace with your repository URL
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'selenium>=4.25.0',
        'webdriver-manager>=4.0.2',
        'beautifulsoup4>=4.12.3',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
