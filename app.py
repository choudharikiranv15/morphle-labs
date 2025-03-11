from flask import Flask
import os
import datetime
import subprocess
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv("CODESPACE_NAME", "Unknown User")

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Get top output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = str(e)

    # Build HTML content
    html_content = f"""
    <html>
        <body>
            <h1>Server Information</h1>
            <p><strong>Name:</strong> Kiran Choudhari</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <pre><strong>Top Output:</strong><br>{top_output}</pre>
        </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
