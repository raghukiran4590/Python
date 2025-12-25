import requests
import json
import urllib3
import datetime
import os

try:

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url = "https://emep-services.anthem.com/misc/utilityfaxnmail/members/JKJKJDS8989389383/email-utility"
    headers = {"Content-Type": "application/json"}
    attachment_path = "/Users/AF35861/Downloads/AWS/test.txt"
    attachment_file = "test.txt"

    # with open(attachment_path, 'rb') as attachment_file:
    #     files = {
    #             "attachment": (os.path.basename(attachment_path), attachment_file, "text/plain")
    #         }
    
            
    body = {
        'staticData': {
            'fromEmail': 'raghu.kiran@elevancehealth.com',
            # 'toEmail': ['Riya.Kumari@carelon.com','GebinB.Tom@carelon.com'],
            'toEmail' : ['raghu.kiran@elevancehealth.com'],
            'ccEmail': ['raghu.kiran@elevancehealth.com'],
            'subject': f"AWS Files {datetime.date.today().strftime("%d/%m/%Y")}",
            'body': {'content': f"Today's AWS Files. <br><br>Thanks", 'bodyContentType': 'HTML', 'toMarkSecure': 'false'}
        },
        'dynamicData': {
            'inLineResource': [{
                'data': {'content': 'test,test2,tes3\n,tes4,tes5,test6', 'filetype': 'txt', 'encoding': 'none'},
                'inLineResourceID': 'Deployment Details Report',
                'archiveResource': 'none'
            }]
        }
    }

    response = requests.request("POST", url, data=json.dumps(body), headers=headers, verify=False)

    if response.status_code == 200:
        print("Email sent successfully")
    else:
        print(f"Failed to send email: {response.reason}")

except FileNotFoundError:
    print(f"Error: The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")