from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "Hello World!"

@app.route('/')
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()