import os
import json
import time
import schedule
from datetime import datetime
from dotenv import load_dotenv
import tweepy

# Load configurations
load_dotenv()
with open('config.json') as f:
    config = json.load(f)

# Initialize Twitter client
def get_twitter_client():
    return tweepy.Client(
        bearer_token=os.getenv('X_BEARER_TOKEN'),
        consumer_key=os.getenv('X_API_KEY'),
        consumer_secret=os.getenv('X_API_SECRET'),
        access_token=os.getenv('X_ACCESS_TOKEN'),
        access_token_secret=os.getenv('X_ACCESS_SECRET')
    )

# For media uploads (different auth method)
def get_twitter_auth():
    return tweepy.OAuth1UserHandler(
        os.getenv('X_API_KEY'),
        os.getenv('X_API_SECRET'),
        os.getenv('X_ACCESS_TOKEN'),
        os.getenv('X_ACCESS_SECRET')
    )

# Load posts from JSON
def load_posts():
    try:
        with open('post.json', 'r') as f:
            posts = json.load(f)
            print(f"📦 Loaded {len(posts)} posts from queue")
            return posts
    except Exception as e:
        print(f"❌ Error loading posts: {e}")
        return []

# Upload image to Twitter
def upload_media(image_path):
    try:
        auth = get_twitter_auth()
        api = tweepy.API(auth)
        media = api.media_upload(image_path)
        return media.media_id
    except Exception as e:
        print(f"❌ Failed to upload media: {e}")
        return None

# Post a single tweet
def post_tweet(text, image_path=None):
    client = get_twitter_client()
    attempts = 0
    
    while attempts < config['max_attempts']:
        try:
            # Handle image if provided
            media_ids = []
            if image_path and os.path.exists(image_path):
                media_id = upload_media(image_path)
                if media_id:
                    media_ids.append(media_id)
                else:
                    print("⚠️ Proceeding without image")
            
            # Send tweet
            response = client.create_tweet(
                text=text,
                media_ids=media_ids if media_ids else None
            )
            
            # Log success
            log_post(text, image_path)
            print(f"✅ Posted: {text[:30]}...")
            return True
            
        except Exception as e:
            attempts += 1
            print(f"⚠️ Attempt {attempts} failed: {e}")
            time.sleep(5)
    
    print(f"❌ Failed after {config['max_attempts']} attempts")
    return False

# Log successful posts
def log_post(text, image_path):
    log_entry = {
        "text": text,
        "image": image_path,
        "posted_at": datetime.now().isoformat()
    }
    
    try:
        with open('posted.log', 'a') as f:
            f.write(json.dumps(log_entry) + "\n")
    except:
        print("⚠️ Could not update log file")

# Process the next tweet in queue
def process_queue():
    posts = load_posts()
    if not posts:
        print("🔄 Queue is empty")
        return
    
    next_post = posts[0]
    
    # Check scheduled date if specified
    if 'scheduled_date' in next_post:
        scheduled_date = datetime.strptime(next_post['scheduled_date'], '%Y-%m-%d').date()
        if scheduled_date > datetime.now().date():
            print(f"⏳ Post scheduled for {next_post['scheduled_date']}")
            return
    
    # Post the tweet
    success = post_tweet(next_post['text'], next_post.get('image'))
    
    # Remove from queue if successful
    if success:
        updated_posts = posts[1:]
        with open('post.json', 'w') as f:
            json.dump(updated_posts, f, indent=2)

# Main scheduler
def run_scheduler():
    print(f"⏰ Scheduler started. Posting every hour")
    schedule.every().hour.do(process_queue)
    
    # Post immediately when starting
    print("🚀 Posting first tweet immediately...")
    process_queue()
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    run_scheduler()