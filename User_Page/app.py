from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html", name="Home", show_message = True)

@app.route("/contact")
def contact():
    return render_template("contact.html", name="Contact")

@app.route("/animal")
def animal():
    zoo_animals = ["Lion", "Giraffe", "Fish", "Elephant"]
    return render_template("animal.html", name="Animal in the zoo", animals = zoo_animals)

@app.route("/about")
def about():
    return render_template("about.html", name="About")

if __name__ == "__main__":
    app.run(debug=True)