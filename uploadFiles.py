import os
import dropbox
from dropbox.files import WriteMode

class TransferData :
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    file_from = input('Enter the file from where you want to upload the file to the google dropbox = ')
    file_to = input('Enter the path where you want to fill the file taken above = ')
    access_token = input('Enter the access token = ')
    transferData = TransferData(access_token)
    transferData.upload_file(file_from, file_to)
    print("File Successfully uploaded")
main()
