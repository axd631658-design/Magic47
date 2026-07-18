import os
import tempfile

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def save_uploaded_file(uploaded_file):
    extension = os.path.splitext(uploaded_file.name)[1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=extension,
        dir=UPLOAD_FOLDER
    ) as temp:
        temp.write(uploaded_file.read())
        return temp.name
