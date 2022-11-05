from ast import dump
from flask import * 
from glob import glob 
import os
from io import BytesIO
from zipfile import ZipFile




app = Flask(__name__) 

app.static_folder = 'static'

UPLOAD_FOLDER = r"D:\xamppnew\htdocs\cv-man\UPLOAD_FOLDER"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

keyword = []

@app.route('/')  
def index(): 
    return render_template("index.html")  

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))  
        key = request.form['k']  
        return render_template("keywords.html", number = int(key))  




@app.route('/submitted', methods = ['POST'])  
def submitted():
    from main import mainf  
    if request.method == 'POST':
        keyword.append(request.form.getlist('kw'))
        mainf()
        re = r'D:\xamppnew\htdocs\cv-man\result\\'
        stream = BytesIO()
        with ZipFile(stream, 'w') as zf:
            for file in glob(os.path.join(re, '*.pdf')):
                zf.write(file, os.path.basename(file))
        stream.seek(0)

        return send_file(
            stream,
            as_attachment=True,
            download_name='archive.zip')
    


if __name__ == '__main__':  
    app.run(host= 'localhost', debug = True) 


