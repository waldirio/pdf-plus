from flask import Flask, render_template, request, redirect, send_file, url_for
from pdfplus import pdfplus, general

mypdf = pdfplus.PdfPlus()
mypdf_obj = general.General()

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check which button was clicked
        if request.form.get('upload'):
            response = mypdf.upload_files()
            print(f"AUDIT: Response from upload: {response}")
            if response == "no_file":
                return mypdf_obj.apology("No File Selected")
            elif response == "not_allowed_ext":
                return mypdf_obj.apology("Extension Not Supported")
            elif response == "no_files_uploaded":
                return mypdf_obj.apology("No File Uploaded")
            elif response == "upload_successfully":
                print(f"AUDIT: Response from upload: {response}")
                # return redirect("/")
                return redirect(url_for('.index', response=response))
                # return render_template("index.html", response=response, mypdf=mypdf)

        elif request.form.get('merge'):
            response = mypdf.merge_files()
            if response:
                return redirect("/")
            else:
                return mypdf_obj.apology("OMG")

        elif request.form.get('download'):
            response = mypdf.download_file()
            if response == "file_not_found":
                return mypdf_obj.apology("File Not Found")
            else:
                return send_file(response, as_attachment=True)

        elif request.form.get('delete'):
            response = mypdf.delete_files()
            print(f"AUDIT: response from delete: {response}")
            if response == "files_deleted":
                return redirect("/")
            else:
                return mypdf_obj.apology("Problems Removing the Files!")


    else:
        response = request.args.get('response')
        return render_template('index.html', response=response, mypdf=mypdf)
