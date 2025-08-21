from flask import Flask

app = Flask(__name__)

# Fake sensitive information (for learning only!)
USERNAME = "admin"
PASSWORD = "P@ssw0rd123"
API_KEY = "fake-api-key-123456"
INTERNAL_IP = "192.168.1.10"

@app.route("/")
def home():
    return f"""
    <h1>Flask Demo App</h1>
    <p><b>Username:</b> {USERNAME}</p>
    <p><b>Password:</b> {PASSWORD}</p>
    <p><b>API Key:</b> {API_KEY}</p>
    <p><b>Internal IP:</b> {INTERNAL_IP}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
