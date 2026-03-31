from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint for ranking
@app.route('/api/rank', methods=['POST'])
def rank():
    data = request.get_json()
    # process ranking logic here
    return {'status': 'success', 'rank': data['rank']}

# API endpoint for score saving
@app.route('/api/save_score', methods=['POST'])
def save_score():
    data = request.get_json()
    # process score saving logic here
    return {'status': 'success', 'score_saved': data['score']}

if __name__ == '__main__':
    app.run(debug=True)