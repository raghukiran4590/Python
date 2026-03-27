import base64
import json
import logging
import requests
from datetime import date

logging.basicConfig(level=logging.INFO)

def encode_file_to_base64(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_bytes = file.read()

        encoded_bytes = base64.b64encode(file_bytes)
        encoded_string = encoded_bytes.decode('utf-8')
        return encoded_string
    # return base64.b64encode(f.read()).decode("utf-8")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

todays_date = date.today().strftime("%Y_%m_%d")
subject_line_date = date.today().strftime("%B %d, %Y")
zip_to_encode = './azure_resource_data_' + todays_date + '.zip'
zip_folder = encode_file_to_base64(zip_to_encode)

url = "https://emep-services.anthem.com/misc/utilityfaxnmail/members/JKJKJDS8989389383/email-utility"
# url = "https://api.digitalproducts.ps.awsdns.internal.das/v1/members/ehds/email-utility"

headers = {
    'User-Agent': 'EDBG-Python-App/1.0',
    # 'apiKey': 'YQlto5s0kEyAPAEAzB2zQx5o5vXLGh3I',
    'Content-Type': 'application/json'
}


body = {
    "staticData": {
        "fromEmail": "noreply@elevancehealth.com",
        # "toEmail": ["Damacharla.Nagajyothi@carelon.com"],
        "toEmail": ["dl-infohub-support@anthem.com"],
        # "ccEmail": ["raghu.kiran@elevancehealth.com"],
        "ccEmail": ["james.strange@elevancehealth.com"],
        "subject": " Azure Data Extract for " + subject_line_date,
        "body": {
            "bodyContentType": "HTML",
            "content": "Hello, " + "<br><br>" +
            "Please find the attached Azure Data Extract for " + subject_line_date + ". "
            "The archive contains files for various Azure resources extracted using Azure Resource Graph. " + "<br><br>" +
            "Let me know if you have any questions or need further information." + "<br><br>Thanks & Regards,<br>Raghu Kiran",
            # "priority": "High",
            "importance": "High",
            "toMarkSecure": "false"
        }
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
                    "inLineResourceID": "azure_data_extract_" + todays_date
            }
        ]
    }
}
response = requests.request("POST", url, data=json.dumps(body), headers=headers, verify=False)
if response.status_code == 200:
    logging.info("Email sent successfully")
else:
    logging.info(f"Failed to send email : {response.reason}")