import os
import sys
from flask import Flask, render_template, request, jsonify
import webview
import subprocess
import threading

pipx_bin_path = os.path.join(os.path.expanduser("~"), ".local", "pipx", "venvs")
flask_path = os.path.join(pipx_bin_path, "flask", "lib", "python3.11", "site-packages")
pywebview_path = os.path.join(pipx_bin_path, "pywebview", "lib", "python3.11", "site-packages")

sys.path.extend([flask_path, pywebview_path])

template_path = os.path.join(os.getcwd(), 'frontend')
static_path = os.path.join(os.getcwd(), 'frontend')

app = Flask(__name__, template_folder=template_path, static_folder=static_path)

@app.route('/')
def index():
    return render_template('zephyr.html')

def internal_server():
    print("Starting internal server...")
    app.run(debug=False)
    print("Internal server started!")

def frontend():
    webview.create_window("Zephyr Nextgen", "http://127.0.0.1:5000", width=1300, height=800)
    print("Zephyr Nextgen done loading!")
    webview.start()

if __name__ == '__main__':
    print("Welcome to Zephyr Nextgen!")
    print("Loading Zephyr Nextgen...")
    print("template_path: ", template_path)
    print("static_path: ", static_path)
    internal_server_thread = threading.Thread(target=internal_server)
    internal_server_thread.daemon = True
    internal_server_thread.start()
    frontend()