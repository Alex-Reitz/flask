from flask import Flask, request

app = Flask(__name__)


@app.route("/hello")
def say_hello():
    html = """
        <h1>Hello There</h1>
    """
    return html


@app.route("/")
def home_page():
    return "This is home page"


@app.route("/search")
def search():
    term = request.args["term"]
    return f"<h1>Search results for: {term} </h1>"


@app.route('/post', methods=["POST"])
def post():
    return "Post DEMO"


@app.route("/add-comment")
def addComment():
    return """
    <form method="POST">
    <input name="comment" type="text" placeholder="something" />
    <input name="username" type="text" placeholder="something" />
    <button>Submit</h1>
    </form>

    """


@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment = request.form["comment"]
    print(request.form)
    return f"""
        <h1>Saved your comment: {comment} </h1>
    """


@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f"This is {subreddit}"


@app.route("/r/<subreddit>/comments/<int:post_id>")
def show_comments(subreddit, post_id):
    return f"{post_id}, {subreddit}"


POSTS = {
    1: "STRING 1",
    2: "STRING 2",
    3: "STRING 3",
    4: "STRING 4"
}


@app.route("/posts/<int:id>")
def find_post(id):
    post = POSTS[id]
    return f"<p>{post}</p>"
