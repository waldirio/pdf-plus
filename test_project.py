import os
import shutil
from pdfplus import pdfplus, general

mypdf = pdfplus.PdfPlus()
mypdf_obj = general.General()

TEMP_FILES_FOLDER = "temp_files"
OUTPUT_FOLDER = "static"
OUTPUT_FILE = OUTPUT_FOLDER + "/out-basic.pdf"


def test_get_count_list_files__no_file():
    """
    Empty input folder (counting the number of files, it should be zero)
    """
    if os.path.exists(TEMP_FILES_FOLDER):
        shutil.rmtree(TEMP_FILES_FOLDER)
        os.mkdir(TEMP_FILES_FOLDER)

    assert mypdf.get_count_list_files() == 0


def test_get_list_files__no_file():
    """
    Empty input folder (it should be an empty list == [])
    """
    if os.path.exists(TEMP_FILES_FOLDER):
        shutil.rmtree(TEMP_FILES_FOLDER)
        os.mkdir(TEMP_FILES_FOLDER)

    assert mypdf.get_list_files() == []


def test_get_count_list_files__with_file():
    """
    Single file in the temp folder (counting the number of files, it should be 1)
    """
    if os.path.exists(TEMP_FILES_FOLDER):
        shutil.rmtree(TEMP_FILES_FOLDER)
        os.mkdir(TEMP_FILES_FOLDER)
        with open(f"{TEMP_FILES_FOLDER}/file1.pdf", "w") as file:
            ...

    assert mypdf.get_count_list_files() == 1


def test_get_list_files__with_file():
    """
    Single file in the temp folder (it should be an empty list == ['file1.pdf'])
    """
    if os.path.exists(TEMP_FILES_FOLDER):
        shutil.rmtree(TEMP_FILES_FOLDER)
        os.mkdir(TEMP_FILES_FOLDER)
        with open(f"{TEMP_FILES_FOLDER}/file1.pdf", "w") as file:
            ...

    assert mypdf.get_list_files() == ['file1.pdf',]


def test_is_output_file__no_file():
    """
    Testing the function once there is no output file (it should be False)
    """
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
        # with open(OUTPUT_FILE, "w") as file:
        #     ...
    assert mypdf.is_output_file() == False


def test_is_output_file__with_file():
    """
    Testing the function once there is an output file (it should be True)
    """    
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
    with open(OUTPUT_FILE, "w") as file:
        ...
    assert mypdf.is_output_file() == True


def test_cleanup_left_over():
    """
    Just to cleanup some left over
    """
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    if os.path.exists(TEMP_FILES_FOLDER):
      shutil.rmtree(TEMP_FILES_FOLDER)
