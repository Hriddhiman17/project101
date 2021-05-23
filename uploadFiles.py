import dropbox

class TransferData :
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    file_from = input('Enter the file from where you want to upload the file to the google dropbox = ')
    file_to = input('Enter the path where you want to fill the file taken above = ')
    access_token = input('Enter the access token = ')
    transferData = TransferData(access_token)
    transferData.upload_file(file_from, file_to)
    print("File Successfully uploaded")
main()
