import os
from flask import Flask
from flask import flash, render_template, request, redirect
from werkzeug.utils import secure_filename
from pyPDF2 import pdfFileReader, pdfFileWriter


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
allowed_file = 'pdf'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'files[]' not in request.files:
            flash('No files found, try again.')
            return redirect(request.url)
        files = request.files.getlist('files[]')
        #for file in files:
           # if file and allowed_file(file.filename):
                #filename = secure_filename(file.filename)
              #  file.save(os.path.join(upload_dest, filename))
        flash('File(s) uploaded')
        return redirect('/upload')

def merge_pdfs(files, output):
    pdf_writer = pdfFileWriter()

    for path in files:
        pdf_reader = pdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    merge_pdfs(files, output='merged.pdf')
    app.run(debug = "true" )
