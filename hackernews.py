import requests

def get_latest_story():
    # Get the latest story ID from the 'newstories' endpoint
    new_stories_url = "https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty"
    response = requests.get(new_stories_url)
    if response.status_code == 200:
        new_stories = response.json()
        latest_story_id = new_stories[0]
        
        # Get the details of the latest story
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{latest_story_id}.json?print=pretty"
        story_response = requests.get(story_url)
        if story_response.status_code == 200:
            story = story_response.json()
            if story and story.get('type') == 'story':
                title = story.get('title')
                author = story.get('by')
                link = story.get('url')
                print(f"Title: {title}")
                print(f"Author: {author}")
                print(f"Link: {link}")
            else:
                print("The latest item is not a story.")
        else:
            print("Failed to fetch the latest story details.")
    else:
        print("Failed to fetch the list of new stories.")

if __name__ == "__main__":
    get_latest_story()

