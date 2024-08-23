from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='template2')

all_topics = [
    "fashion", "health", "travel", "music", "movies", "technology", "food", "sports",
    "art", "science", "gaming", "fitness", "nature", "books", "photography", "history",
    "cars", "news", "diy", "pets"
]

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        selected_topics = request.form.getlist('topics')
        if len(selected_topics) == 5:
            return redirect(url_for('filtered_content', topics=selected_topics))
        else:
            return "Please select exactly 5 topics.", 400
    return render_template('signup.html')

@app.route('/filtered-content')
def filtered_content():
    topics = request.args.getlist('topics')
    posts = get_posts_related_to(topics)
    return render_template('content.html', posts=posts)

@app.route('/signup-uninterested', methods=['GET', 'POST'])
def signup_uninterested():
    if request.method == 'POST':
        uninterested_topics = request.form.getlist('topics')
        if len(uninterested_topics) == 5:
            interested_topics = [topic for topic in all_topics if topic not in uninterested_topics]
            return redirect(url_for('filtered_content_interested', topics=interested_topics))
        else:
            return "Please select exactly 5 topics.", 400
    return render_template('template2/signup_uninterested.html')

@app.route('/filtered-content-interested')
def filtered_content_interested():
    topics = request.args.getlist('topics')
    posts = get_posts_related_to(topics)
    return render_template('template2/content.html', posts=posts)

def get_posts_related_to(topics):
    posts = [
        # Example content, ensure these are relevant
    ]

    filtered_posts = [post for post in posts if any(tag in topics for tag in post['tags'])]
    return filtered_posts

if __name__ == '__main__':
    app.run(debug=True)
