import os


UPLOAD_FOLDER = "uploads"


def save_uploaded_files(uploaded_files):

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    for file in uploaded_files:

        filepath = os.path.join(
            UPLOAD_FOLDER,
            file.name
        )

        with open(filepath, "wb") as f:

            f.write(file.getbuffer())

    return UPLOAD_FOLDER

def clear_uploads():

    if not os.path.exists(UPLOAD_FOLDER):
        return

    for file in os.listdir(UPLOAD_FOLDER):

        filepath = os.path.join(
            UPLOAD_FOLDER,
            file
        )

        os.remove(filepath)