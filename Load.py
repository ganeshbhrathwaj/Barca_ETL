from Google import Create_Service
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import requests
import json
from apiclient import errors
from apiclient.http import MediaFileUpload

def upload():
        CLIENT_SECRET_FILE='client_secrets.json'
        API_NAME='drive'
        API_VERSION='v3'
        scopes=["https://www.googleapis.com/auth/drive"]
        webhook = "https://hooks.slack.com/services/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"
        
        folder_id='1lQXGp1oDhvFL8PxP3plYoi1kAJfmCpgC'
        file_name='barca_stats.xlsx'
        file_id='1WPReMnJ3T5ZGDuUH0cm6i63Wd47x9HKP'
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

        service=Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,scopes)
        gauth = GoogleAuth()           
        drive = GoogleDrive(gauth)

        listed = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1lQXGp1oDhvFL8PxP3plYoi1kAJfmCpgC')}).GetList()
        for file in listed:
                if "barca_stats.xlsx" not in file['title']:
                        print('UPLOADING THE NEW FILE')
                        #service.files().delete(fileId=file['id']).execute()
                        '''gfile = drive.CreateFile({'parents': [{'id': folder_id}]})
                        gfile.SetContentFile(file_name)
                        gfile.Upload()
                        payload = {"text": "NEW FILE UPLOADED IN GDRIVE"}'''
                else:
                        print("UPDATING THE FILE - ",file_id)
                        old_file = drive.CreateFile({'id': file_id, 'mimeType': mime})
                        old_file.SetContentFile(file_name)
                        old_file.Upload()
                        payload = {"text": "FILE UPDATED IN GDRIVE"}

                        
        requests.post(webhook, json.dumps(payload))

if __name__ == '__main__':
        upload()





