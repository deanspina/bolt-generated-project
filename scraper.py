import requests
    from bs4 import BeautifulSoup

    def scrape_linkedin_profile(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extracting name
            name_tag = soup.find('h1', class_='text-heading-xlarge inline t-24 v-align-middle break-words')
            name = name_tag.get_text(strip=True) if name_tag else 'N/A'
            
            # Extracting title
            title_tag = soup.find('h2', class_='text-heading-medium break-words')
            title = title_tag.get_text(strip=True) if title_tag else 'N/A'
            
            # Extracting location
            location_tag = soup.find('span', class_='text-body-small inline-block text-secondary-text')
            location = location_tag.get_text(strip=True) if location_tag else 'N/A'
            
            # Extracting summary
            summary_tag = soup.find('div', class_='pv-shared-text-with-see-more-v2 break-words')
            summary = summary_tag.get_text(strip=True) if summary_tag else 'N/A'
            
            return {
                'name': name,
                'title': title,
                'location': location,
                'summary': summary
            }
        else:
            print(f"Failed to retrieve the profile. Status code: {response.status_code}")
            return None

    if __name__ == "__main__":
        url = input("Enter LinkedIn profile URL: ")
        profile_data = scrape_linkedin_profile(url)
        
        if profile_data:
            print("\nProfile Data:")
            for key, value in profile_data.items():
                print(f"{key.capitalize()}: {value}")
