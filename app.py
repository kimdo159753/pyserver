from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/save-memo', methods=['POST'])
def save_memo():
    pass

if __name__ == "__main__":
    app.run()
