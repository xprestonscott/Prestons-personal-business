from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    """The sell-websites page: hero cinematic + the three concepts.

    NOTE: the concept switcher (01/02/03) is visible to real visitors here.
    Once a concept is chosen, drop the other two and delete #switch.
    """
    return render_template('work.html')

@app.route('/classic')
def classic():
    """The previous homepage — hero + Never Miss a Job. Kept so nothing that
    was live before this switch is lost."""
    return render_template('index.html')

@app.route('/system')
def system():
    """Never Miss a Job — the productized missed-call/lead-capture offer."""
    return render_template('system.html')

@app.route('/work')
def work():
    """Working draft: three concepts for the sell-websites model, plus the
    anonymised work gallery. Not linked from anywhere and noindexed."""
    return render_template('work.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Basic handler so the form doesn't crash if it's wired up later.
    data = request.form.to_dict()
    print("Form submission received:", data)
    return jsonify({"success": True})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)