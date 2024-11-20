# LinkedIn Scraper

    ## Overview

    A simple Python script to scrape LinkedIn profiles.

    ## Installation

    1. Clone the repository:
       ```bash
       git clone https://github.com/yourusername/linkedin-scraper.git
       cd linkedin-scraper
       ```

    2. Build and run the Docker container:
       ```bash
       docker build -t linkedin-scraper .
       docker run -it --rm linkedin-scraper
       ```

    ## Usage

    1. Enter a LinkedIn profile URL when prompted.
    2. The script will scrape and display the name, title, location, and summary of the profile.

    ## Notes

    - **Rate Limiting**: Be mindful of LinkedIn's rate limits.
    - **Legal Considerations**: Ensure you have permission to scrape the data from LinkedIn profiles.
    - **Dynamic Content**: LinkedIn uses JavaScript to load content dynamically. This script might not work for all profiles due to this reason.
