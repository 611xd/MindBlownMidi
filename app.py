from flask import Flask, render_template, request
from midonum import midinum
import os
from werkzeug import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = './data'
app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER

@app.route("/",methods=['POST'])
def index_post():
    uploadfile = request.files['file']
    filename = secure_filename(uploadfile.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    uploadfile.save(filepath)
    output = midinum(filepath)
    return render_template('end.html', greet=output)

@app.route("/",methods=['GET'])
def index_get():
    return render_template('upload.html')


if __name__ == "__main__":
    app.run()
