import base64
import json
import logging
import requests

logging.basicConfig(level=logging.INFO)

def encode_file_to_base64(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_bytes = file.read()

        encoded_bytes = base64.b64encode(file_bytes)
        encoded_string = encoded_bytes.decode('utf-8')
        return encoded_string

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

zip_to_encode = '/Users/AF35861/Downloads/azure_resource_data/azure_resource_data_2026_03_16.zip'
file_to_encode = 'file.txt'
zip_folder = encode_file_to_base64(zip_to_encode)
file_content = encode_file_to_base64(file_to_encode)

# url = "https://emep-services.anthem.com/misc/utilityfaxnmail/members/JKJKJDS8989389383/email-utility"
url = "https://api.digitalproducts.ps.awsdns.internal.das/v1/members/ehds/email-utility"

headers = {
    'User-Agent': 'EDBG-Python-App/1.0',
    'apiKey': 'YQlto5s0kEyAPAEAzB2zQx5o5vXLGh3I',
    'Content-Type': 'application/json'
}

body = {
    "staticData": {
        "ccEmail": ["raghu.kiran@elevancehealth.com"],
        "subject": " Test Email",
        "body": {
            "bodyContentType": "HTML",
            "content": "Job is completed. <br><br>Thanks",
            "toMarkSecure": "false"
        },
        "toEmail": [
            "raghu.kiran@elevancehealth.com"
        ],
        "fromEmail": "noreply@anthem.com",
    },
        "dynamicData": {
        "inLineResource": [
            {
                "data":
                    {
                        "content": zip_folder,
                        "filetype": "ZIP",
                        "encoding": "BASE64"
                    },
                    "inLineResourceID": "Data1"
            },
            {
                "data":
                    {
                        "content": file_content,
                        "filetype": "TXT",
                        "encoding": "BASE64"
                    },
                    "inLineResourceID": "Data2"
            }
        ]
    }
}
response = requests.request("POST", url, data=json.dumps(body), headers=headers, verify=False)
if response.status_code == 200:
    logging.info("Email sent successfully")
else:
    logging.info(f"Failed to send email : {response.reason}")