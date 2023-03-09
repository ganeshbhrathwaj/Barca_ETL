import Extract as ex
import requests
import json

#import Load
if __name__ == '__main__':
        ex.extract_ga()
        ex.yellow_red()
        ex.squard_stats()
        ex.laliga_table()
        ex.load_temp()
        #Load.upload()
        webhook = "https://hooks.slack.com/services/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"
        payload = {"text": "FILE UPDATED"}
        requests.post(webhook, json.dumps(payload))
        
