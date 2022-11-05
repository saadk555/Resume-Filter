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
        f = request.files.getlist("file")
        for i in f:
            i.save(os.path.join(app.config['UPLOAD_FOLDER'], i.filename))  
        key = request.form['k']  
        return render_template("keywords.html", number = int(key))  




@app.route('/submitted', methods = ['POST'])  
def submitted():
    from main import mainf  
    if request.method == 'POST':
        keyword.append(request.form.getlist('kw'))
        mainf(keyword)
        re = r'D:\xamppnew\htdocs\cv-man\result\\'
        #stream = BytesIO()
        with ZipFile(r"D:\xamppnew\htdocs\cv-man\result\result.zip", 'w') as zip:
            for file in glob(os.path.join(re, '*.pdf')):
                zip.write(file, os.path.basename(file))
        #stream.seek(0)
        @after_this_request
        def remove_file(response):
            file_path = r'D:\xamppnew\htdocs\cv-man\result\*.pdf'
            try:
                os.remove(file_path)
            except Exception as error:
                app.logger.error("Error removing or closing downloaded file handle", error)
            return response
        return render_template("result.html")

        return send_file(
            stream,
            as_attachment=True,
            download_name='archive.zip')


@app.route('/result', methods = ['GET']) 
def result():
    @after_this_request
    def remove_file(response):
        file_path = r'D:\xamppnew\htdocs\cv-man\result\result.zip'
        try:
            os.remove(file_path)
        except Exception as error:
            app.logger.error("Error removing or closing downloaded file handle", error)
        return response
    if request.method == 'GET':
        download = r"D:\xamppnew\htdocs\cv-man\result\result.zip"
        return send_file(download, as_attachment=True)

    


if __name__ == '__main__':  
    app.run(host= 'localhost', debug = True) 


