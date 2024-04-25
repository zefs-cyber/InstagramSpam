import instaloader
import pandas as pd
from setting import LOGIN, PASSWORD, PAGES

# Create an instance of Instaloader class
L = instaloader.Instaloader()

# Optionally, log in to Instagram (replace 'your_username' and 'your_password' with your credentials)
L.login(LOGIN, PASSWORD)  # Login is sometimes necessary to bypass limitations

page_names = []
post_links = []

for page in PAGES:
    # Load a profile
    profile = instaloader.Profile.from_username(L.context, page)
    i = 0

    # Fetch and print all post URLs
    for post in profile.get_posts():
        post_page_url = f"https://www.instagram.com/p/{post.shortcode}/"
        page_names.append(page)
        post_links.append(post_page_url)
        i += 1
    
    print(f'Done with - {page}/ total number of posts - {i}')

df = pd.DataFrame({'page_names': page_names, 'post_links': post_links})
df.to_excel('links.xlsx', index=False)