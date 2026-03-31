# Flask application with routes and score management
from flask import Flask, render_template, jsonify

app = Flask(__name__)

score = 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/score')
def get_score():
    return jsonify(score=score)

@app.route('/update_score', methods=['POST'])
def update_score():
    global score
    # Logic to update the score
    score += 10  # Example increment
    return jsonify(score=score)

if __name__ == '__main__':
    app.run(debug=True)