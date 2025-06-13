from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace these with your actual keys
API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiOWI4MzNhMmE2MjI2ZDlhNmI2OWNmNGNiNGRkODdkMDQ4OWQxZDViYmI3M2VmNzdiZGZjODI0MmFmNDBkN2JiZTAxMmU4YjQ0YmRiOTVhODMiLCJpYXQiOjE3NDk3NjY5MDYuMDMxNzUzLCJuYmYiOjE3NDk3NjY5MDYuMDMxNzU3LCJleHAiOjQ5MDU0NDA1MDYuMDI3NjM2LCJzdWIiOiIxNjAyMTY2Iiwic2NvcGVzIjpbXX0.C3xwDuqOdDKY25FYrzVQUmgC2TgikNFjQvChksncW6qc2f0jmyaX4nrkVzKUJ6-sYeRRIv0xocQrABBFQelovsLiGQFrv1UrR7QMy6raAhv8IZImOy8DUC35XGUj5U41bINK4GCtQcqEcfzu1DlhPc15dL-D6lZa4p5FYLAYgxRRKV6G28isocZ1iFRcDGJekDpUypfOAjj3ZEk3MD80Liq_EZkAwcFOg4HiLWJRvMpnd9CaR18NR6S-LiQ5WRuSJXZcYIgwRaz4jTrG2wVnPPqNUenAQ3PHtXe4n8RXcdpkAlg1_ybbuuE6et9SrOEoG3hHzkdNfsvS5hIQvRG1-hr812JzytzSJ6tyST8xnE4m4EmcfKUQMx7z28OFPgQYa0EatQnhDkZL1ozIz5ZK4CJDelPSTaakLYyWbReVUGe5AWk5q90kt2vzVuK8ua8swry3VHnBKWe3YZAmAxa-FVYm-Fy3yrxQ0yDi30Opl_RSs79XODCFX3xHx5ApkmkexbA5N27XKyRyUuUZ-Ow5ZYfUOKIGhpQ9bXlkS7c855AR2h9027FNodSA4BPBPTqYAv3ygw75WIbxAnJcZqqZlSEYxOLpNw1Wx3sHdbFC1k3fEOPbiz0UGJf1qEWFt3Z_Tx-z6n-gq7XDH1_L-kRZFnWCRFAcRkHU1CmNTKE06_Q"
GROUP_ID = "157041339585791070"

@app.route("/")
def home():
    return jsonify({"message": "Flask webhook server is running", "status": "active"})

@app.route("/ghl-webhook", methods=["POST"])
def ghl_webhook():
    data = request.get_json()

    email = data.get("email")
    name = data.get("name", "No Name")

    if not email:
        return jsonify({"error": "Missing email"}), 400

    payload = {
        "email": email,
        "name": name,
        "groups": [GROUP_ID],
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.post(
        "https://api.mailerlite.com/api/v2/subscribers",
        json=payload,
        headers=headers
    )

    return jsonify({
        "mailerLiteStatus": response.status_code,
        "mailerLiteResponse": response.json()
    }), response.status_code

# For local testing (optional)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
