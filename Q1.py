from flask import Flask
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system information
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode()
    user = subprocess.check_output(['whoami']).decode().strip()
    current_time = datetime.datetime.now() + datetime.timedelta(hours=5, minutes=30)
    
    # Create a simpler response with minimal formatting
    return f"""
    Name: Your Full Name
    Username: {user}
    Server Time (IST): {current_time}
    TOP output:
    {top_output}
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
