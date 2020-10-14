from sublate import vtt_translate, srt_translate
import os
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory, send_file
from werkzeug.utils import secure_filename

# set upload folder
UPLOAD_FOLDER = '/home/byte/tmp/subtitle_translate/uploads/'
TRANSLATED_FOLDER = '/home/byte/tmp/subtitle_translate/translated/'
ALLOWED_EXTENSIONS = {"md", "vtt", "srt", "svb"}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#right file
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#/ --> upload file
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # start the translate
            x = filename[:-4]
            y = filename[-4:]
            filename_persian = x + "_persian" + y
            #TODO detect file format
            if y == ".srt":
                t = srt_translate(UPLOAD_FOLDER,TRANSLATED_FOLDER, filename, filename_persian)
            elif y == ".vtt":
                t = vtt_translate(UPLOAD_FOLDER,TRANSLATED_FOLDER, filename, filename_persian)
            elif y == ".sbv":
                pass
            else:
                print("dont detect!!!")

            return redirect(url_for('download_file', filename=t))
    return render_template('upload.html')

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)


@app.route("/downloadfile/<filename>", methods = ['GET'])
def download_file(filename):
    return render_template('download.html',value=filename)

@app.route('/return-files/<filename>')
def return_files_tut(filename):
    file_path = TRANSLATED_FOLDER + filename
    return send_file(file_path, as_attachment=True, attachment_filename='')