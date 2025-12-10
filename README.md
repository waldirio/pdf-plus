# PDF-plus
#### Video Demo: [https://youtu.be/TODO](https://youtu.be/TODO)

# Disclaimer
This is an independent project to help people merge different `PDF` files, and also, created as part of [CS50P](https://pll.harvard.edu/course/cs50s-introduction-programming-python) course, as the final project. The developers are not responsible if your PDF file(s) are corrupt, or not working properly.

# Use Case
It's very common in nowadays we face the necessity to combine multiple PDF files, for legal needs, or even for homework, and sometimes, it's just boring, once there is no simple way to combine them easily.

Also, it's valid to mention that there are many websites providing such service. However, we have no idea where our data is hosted, and if they will still hosted for a while.

With PDF+, you can merge your own `PDF` files, in the comfort of your home, just using this application locally, via virtual environment locally, or even via container (steps will be available below).

# Requirements
The `requirements.txt` specifies the modules required for the application to work properly.

# Features
PDF+ will allow you to:
- Upload multiple `PDF` files;
- Merge all the files, creating a single `PDF`;
- Download it;
- Delete all the files from the application, whenever you wish.

#### Upload multiple `PDF` files:
You can upload one, two, or as many `PDF` files you wish to PDF+ application.

#### Merge all the files, creating a single `PDF`:
Once you have all the files, you can just hit the `Merge` button, and the magic will happen.

#### Download it:
Once you have it merged, the merged `PDF` file will be downloaded, and you should be able to save it locally.

#### Delete all the files from the application, whenever you wish: 
Once you are done, you can hit the button to delete all the files. It will remove all the uploaded files, and also the merged files. Note that this will not delete any file from your local desktop, only the files that were uploaded to `PDF+`.

# Supportability and Results
The system has defined the following as allowed file format:
- PDF

# Code / Functions


**app.py** consists of the following functions:

- `index()`
    - Endpoint that will be handling most of the `POST` calls.

- `about()`
    - Endpoing that will present the `About` page.


The **pdfplus.py** contains the `PdfPlus` Class and Methods:

- `PdfPlus()`
    - Class created to handle all the `PDF+` calls.

- `__init__(self)`
    - Default constructor. At this moment, checking if there is a `temporary folder`, in case not, the same will create it.

- `allowed_file(self, filename)`
    - Method to guarantee that only supported extension will be accepted.

- `upload_files(self)`
    - Method to upload files to the system.

- `merge_files(self)`
    - Method to merge the files that were uploaded by `upload_files()` method.

- `delete_files(self)`
    - Method to delete all the files, from `temporary folder`, and also `merged` file.

- `get_list_files(self)`
    - Method to retrieve the list of files that were uploaded.

- `get_count_list_files(self)`
    - Method to count the number of files that were uploaded.

- `is_output_file(self)`
    - Method to verify if the `merged file` is already available or not.


The **general.py** contains the `General` Class and Methods:

- `General()`
    - Class created to handle all the general of `PDF+` application.

- `apology(self, message, code=400)`
    - Method to present the `custom` error message.


# Application Usage
Just start the application, and access it via webUI on port `5000`. After that, you can:
- Click on `Browse` to pick the file(s) you would like to merge, after that, click on `Upload Files`.
- Click on `Merge Files` to create the `merged` version.
- Click on `Download` to download the `merged` version.
- Click on `Delete Files` to remove all the `temporary files`, and also the `merged` file.

Users who have questions can send messages with questions or suggestions to the contact email `marcellestp@gmail.com` and `waldirio@gmail.com`.

# To Deploy via Virtual Environment
- Create a Python Virtual Environment
```
python3 -m venv ~/.venv/pdf+
```
- Load the Virtual Environment
```
source ~/.venv/pdf+/bin/activate
(pdf+) user@local ~ %
```
- Clone the repo
```
git clone https://github.com/waldirio/pdf-plus.git
cd pdf-plus
```
- Install the Python Modules via Requirements.txt
```
pip install -r requirements.txt
```
- Start the Application
```
flask run --debug
...
* Running on http://127.0.0.1:5000
```


# Reference
- BootStrap
    - https://getbootstrap.com/
- Flask
    - https://flask.palletsprojects.com/
- Python
    - https://docs.python.org/
- Jinja
    - https://jinja.palletsprojects.com/en/stable/
- MarkDown
    - https://www.markdownguide.org/basic-syntax/
- pypdf
    - https://pypdf.readthedocs.io/en/stable/
