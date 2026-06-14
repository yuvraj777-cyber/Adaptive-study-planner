from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendation = None

    if request.method == "POST":
        name = request.form["name"]
        subject = request.form["subject"]
        study_hours = int(request.form["study_hours"])
        quiz_score = int(request.form["quiz_score"])
        mistakes = int(request.form["mistakes"])

        recommendation = []

        if quiz_score < 60:
            recommendation.append(
                f"Increase {subject} study time by 1 hour and revise tomorrow."
            )

        elif quiz_score > 85:
            recommendation.append(
                f"Great performance in {subject}. Revision can be scheduled after 3 days."
            )

        if mistakes > 10:
            recommendation.append(
                f"Prioritize {subject} because many mistakes were detected."
            )

        if not recommendation:
            recommendation.append(
                f"Maintain current study plan for {subject}."
            )

    return render_template(
        "index.html",
        recommendation=recommendation
    )

if __name__ == "__main__":
    app.run(debug=True)
