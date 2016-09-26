from flask import Flask

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return "hello world"

@app.route('/read_temp')
def read_temp():
    file_read = open("temp.txt", "rt")
    temperature = file_read.read()
    file_read.close()

    return temperature

app.run(port=9999, debug=True)