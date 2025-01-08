from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Function to simulate API data
def calculate_pp_from_rank(rank):
    return round(2000 / (rank ** 0.5), 2)

def calculate_rank_from_pp(pp):
    return round((2000 / pp) ** 2)

@app.route("/")
def home():
    return render_template("index.html")  # Ensure your HTML is saved as 'templates/index.html'

@app.route("/rank-to-pp", methods=["POST"])
def rank_to_pp():
    rank = request.form.get("input-rank", type=float)
    if rank:
        pp = calculate_pp_from_rank(rank)
        return jsonify({"pp": pp})
    return jsonify({"error": "Invalid rank provided"})

@app.route("/pp-to-rank", methods=["POST"])
def pp_to_rank():
    pp = request.form.get("input-pp", type=float)
    if pp:
        rank = calculate_rank_from_pp(pp)
        return jsonify({"rank": rank})
    return jsonify({"error": "Invalid PP provided"})

@app.route("/user-stats", methods=["POST"])
def user_stats():
    username = request.form.get("user-statistics")
    # Simulate user data for the demo (replace with real osu! API calls)
    mock_data = {
        "profile_name": username,
        "rank": 1000,
        "pp": 4567.89,
        "plays": 1234,
        "accuracy": "98.76%",
        "country": "JP",
        "level": 100,
    }
    return jsonify(mock_data)

if __name__ == "__main__":
    app.run(debug=True)
