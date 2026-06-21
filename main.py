from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    business_name = request.form.get("business_name", "")
    business_type = request.form.get("business_type", "")
    current_website = request.form.get("current_website", "") or "None"
    main_goal = request.form.get("main_goal", "")
    challenge = request.form.get("challenge", "")
    contact_method = request.form.get("contact_method", "")
    contact_info = request.form.get("contact_info", "")

    entry = (
        f"\n{'='*50}\n"
        f"Submitted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"Business Name: {business_name}\n"
        f"Business Type: {business_type}\n"
        f"Current Website: {current_website}\n"
        f"Main Goal: {main_goal}\n"
        f"Biggest Challenge: {challenge}\n"
        f"Preferred Contact: {contact_method}\n"
        f"Contact Info: {contact_info}\n"
    )

    with open("submissions.txt", "a", encoding="utf-8") as f:
        f.write(entry)

    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
