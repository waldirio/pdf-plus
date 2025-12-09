from flask import request
import tempfile
import os
import shutil
from werkzeug.utils import secure_filename
from pypdf import PdfWriter
from pdfplus import general

TEMP_FOLDER = 'temp_files/'
STATIC = "static/"
FINAL_FILENAME = "out-basic.pdf"
ALLOWED_EXTENSIONS = {'pdf'}

general = general.General()

class PdfPlus():


    def allowed_file(self, filename):
        """
        Ensure that only the defined extensions are accepted when uploading files.
        """
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


    def upload_files(self):
        """
        Upload files selected by the user uploading only files with the allowed extensions.
        """
        # Get the list of files
        files = request.files.getlist('files')
        print(f"AUDIT: files: {files}")
        # Checks if any files are selected
        if not files[0].filename:
            return "no_file"

        elif files:
            temp_dir = tempfile.mkdtemp()
            print(f"AUDIT: temp_dir: {temp_dir}")
            # Save each file to the uploads directory
            for file in files:
                if file and self.allowed_file(file.filename):
                    # secure_filename resolving file with space in name
                    filename = secure_filename(file.filename)
                    # Adding the lower() to avoid issues with the extension
                    # when processing the pdf files
                    file.save(os.path.join(temp_dir, filename.lower()))
                else:
                    # selected not allowed files
                    # return 1
                    print(f"AUDIT: files: {file}")
                    return "not_allowed_ext"

            for file in files:
                # secure_filename resolving file with space in name
                filename = secure_filename(file.filename)
                # Adding the lower() to avoid issues with the extension
                # when processing the pdf files
                print(f"AUDIT: temp_dir: {temp_dir}, TEMP_FOLDER: {TEMP_FOLDER}")
                shutil.copy(os.path.join(temp_dir, filename.lower()), TEMP_FOLDER)
            shutil.rmtree(temp_dir)
            # return 'Files uploaded successfully'
            # print(f"AUDIT: ")
            return 'upload_successfully'
        else:
            return "no_files_uploaded"


    def merge_files(self):
        # Working with pdf merge
        # https://pypdf.readthedocs.io/en/stable/user/merging-pdfs.html
        print(f"AUDIT: Here I'm")
        merger = PdfWriter()
        aux = os.listdir(TEMP_FOLDER)
        print(f"AUDIT: aux: {aux}")
        for pdf in os.listdir(TEMP_FOLDER):
            print(f"AUDIT: File: {pdf}")
            merger.append(TEMP_FOLDER + pdf)

        # Creating the final file, with all the PDF's attached
        merger.write(STATIC + FINAL_FILENAME)
        if os.path.exists(STATIC + FINAL_FILENAME):
            return True
        else:
            return False


    def download_file(self):
        print(f"AUDIT: downloading file")
        if os.path.exists(STATIC + FINAL_FILENAME):
            return STATIC + FINAL_FILENAME
        else:
            return "file_not_found"


    def delete_files(self):
        """
        Delete the existing files in the static directory
        """

        # Check if there are files in the temporary folder
        if os.path.exists(TEMP_FOLDER):
            for filename in os.listdir(TEMP_FOLDER):
                file_path = os.path.join(TEMP_FOLDER, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.remove(file_path)
                except Exception as e:
                    return "error_deleting_input_files"

        # Check if there's an output file to get removed
        PATH_FILE = STATIC + FINAL_FILENAME

        if os.path.exists(PATH_FILE):
            try:
                os.remove(PATH_FILE)
            except:
                return "error_deleting_output_file"
            else:
                return "files_deleted"
    

    def get_list_files(self):
        temp_list = []
        for pdf in os.listdir(TEMP_FOLDER):
            temp_list.append(pdf)
        return temp_list


    def get_count_list_files(self):
        temp_list = []
        for pdf in os.listdir(TEMP_FOLDER):
            temp_list.append(pdf)
        return len(temp_list)


    def is_output_file(self):
        if os.path.exists(STATIC + FINAL_FILENAME):
            return True
        else:
            return False