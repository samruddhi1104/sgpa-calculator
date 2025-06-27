from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        subjects = request.form.getlist("subject")
        credits = request.form.getlist("credit")
        grades = request.form.getlist("grade")

        total_credits = 0
        total_points = 0

        for c, g in zip(credits, grades):
            try:
                c = float(c)
                g = float(g)
                total_credits += c
                total_points += c * g
            except:
                continue

        if total_credits > 0:
            result = round(total_points / total_credits, 2)
        else:
            result = "Invalid input"

    return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)