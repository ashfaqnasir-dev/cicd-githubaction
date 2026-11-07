import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    env_name = os.getenv('APP_ENV', 'Production')
    return f"""
    <div style='text-align: center; margin-top: 60px; font-family: sans-serif;'>
        <h1>🚀 CI/CD Automated Deployment</h1>
        <p>This container was built and published automatically via <b>GitHub Actions</b>!</p>
        <p>Status: <span style='color: green; font-weight: bold;'>Healthy & Live</span></p>
        <p>Environment: <b>{env_name}</b></p>
    </div>
    """

@app.route('/health')
def health():
    return {"status": "ok", "app": "flask-ci-cd"}, 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

