from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='template2')

all_topics = [
    "fashion", "health", "travel", "music", "movies", "technology", "food", "sports",
    "art", "science", "gaming", "fitness", "nature", "books", "photography", "history",
    "cars", "news", "diy", "pets"
]

@app.route('/signup-uninterested', methods=['GET', 'POST'])
def signup_uninterested():
    if request.method == 'POST':
        uninterested_topics = request.form.getlist('topics')
        if len(uninterested_topics) == 5:
            # Determine interested topics by excluding uninterested ones
            interested_topics = [topic for topic in all_topics if topic not in uninterested_topics]
            return redirect(url_for('filtered_content_interested', topics=interested_topics))
        else:
            return "Please select exactly 5 topics.", 400
    return render_template('template2/signup_uninterested.html')

@app.route('/filtered-content-interested')
def filtered_content_interested():
    topics = request.args.getlist('topics')
    posts = get_posts_related_to(topics)
    return render_template('content.html', posts=posts)

def get_posts_related_to(topics):
    # Example of fictional TikTok-style content with topic tags
    posts = [
        {
            "user": "fashionista99",
            "description": "Top 5 Summer Fashion Trends! ☀️ #fashion #trending",
            "video_url": "https://www.example.com/videos/fashion1.mp4",
            "likes": 1200,
            "comments": 300,
            "shares": 150,
            "tags": ["fashion", "trending"],
        },
        {
            "user": "healthyguru",
            "description": "Morning Yoga Routine for Beginners 🧘‍♀️ #health #wellness",
            "video_url": "https://www.example.com/videos/health1.mp4",
            "likes": 1800,
            "comments": 200,
            "shares": 120,
            "tags": ["health", "wellness"],
        },
        {
            "user": "wanderlust_travels",
            "description": "Exploring the Hidden Gems of Bali 🌴 #travel #wanderlust",
            "video_url": "https://www.example.com/videos/travel1.mp4",
            "likes": 2500,
            "comments": 450,
            "shares": 300,
            "tags": ["travel", "wanderlust"],
        },
        {
            "user": "musiclover101",
            "description": "My Top 5 Songs of the Week 🎧 #music #playlist",
            "video_url": "https://www.example.com/videos/music1.mp4",
            "likes": 3200,
            "comments": 600,
            "shares": 400,
            "tags": ["music", "playlist"],
        },
        {
            "user": "moviemagic",
            "description": "Must-Watch Movies This Weekend 🎬 #movies #cinema",
            "video_url": "https://www.example.com/videos/movies1.mp4",
            "likes": 2800,
            "comments": 500,
            "shares": 350,
            "tags": ["movies", "cinema"],
        },
        {
            "user": "techgeek",
            "description": "Unboxing the Latest Smartphone! 📱 #technology #gadget",
            "video_url": "https://www.example.com/videos/tech1.mp4",
            "likes": 4500,
            "comments": 800,
            "shares": 500,
            "tags": ["technology", "gadget"],
        },
        {
            "user": "foodie_heaven",
            "description": "Making the Perfect Homemade Pizza 🍕 #food #cooking",
            "video_url": "https://www.example.com/videos/food1.mp4",
            "likes": 3900,
            "comments": 700,
            "shares": 450,
            "tags": ["food", "cooking"],
        },
        {
            "user": "sportsfanatic",
            "description": "Top 10 Moments from Last Night's Game! 🏀 #sports #highlights",
            "video_url": "https://www.example.com/videos/sports1.mp4",
            "likes": 5000,
            "comments": 900,
            "shares": 600,
            "tags": ["sports", "highlights"],
        },
        {
            "user": "artsy_vibes",
            "description": "Creating a Masterpiece with Acrylic Paints 🎨 #art #creativity",
            "video_url": "https://www.example.com/videos/art1.mp4",
            "likes": 2200,
            "comments": 400,
            "shares": 250,
            "tags": ["art", "creativity"],
        },
        {
            "user": "science_explorer",
            "description": "Amazing Science Experiments You Can Try at Home 🧪 #science #experiments",
            "video_url": "https://www.example.com/videos/science1.mp4",
            "likes": 3300,
            "comments": 550,
            "shares": 350,
            "tags": ["science", "experiments"],
        },
    ]

    # Filter posts based on the selected topics
    filtered_posts = [post for post in posts if any(tag in topics for tag in post['tags'])]

    return filtered_posts

if __name__ == '__main__':
    app.run(debug=True)
