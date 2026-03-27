import base64
import logging
import os
import requests
from datetime import date
 
logging.basicConfig(level=logging.INFO)
 
def encode_file_to_base64(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
 
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
 
def main():
    todays_date = date.today().strftime("%Y_%m_%d")
    subject_line_date = date.today().strftime("%B %d, %Y")
 
    zip_to_encode = './azure_resource_data_' + todays_date + '.zip'
    zip_b64 = encode_file_to_base64(zip_to_encode)
 
    url = "https://emep-services.anthem.com/misc/utilityfaxnmail/members/JKJKJDS8989389383/email-utility"
 
    headers = {
        "User-Agent": "EDBG-Python-App/1.0",
        "Content-Type": "application/json",
    }
 
    body = {
        "staticData": {
            "fromEmail": "raghu.kiran@elevancehealth.com",
            "toEmail": ["dl-infohub-support@anthem.com"],
            "ccEmail": ["james.strange@elevancehealth.com"],
            "subject": f"Azure Data Extract for {subject_line_date}",
            "body": {
                "bodyContentType": "HTML",
                "content": (
                    "Hello,<br><br>"
                    f"Please find the attached Azure Data Extract for {subject_line_date}. "
                    "The archive contains files for various Azure resources extracted using Azure Resource Graph.<br><br>"
                    "Let me know if you have any questions or need further information.<br><br>"
                    "Thanks & Regards,<br>Raghu Kiran"
                ),
                "toMarkSecure": "false",
            },
        },
        "dynamicData": {
            "inLineResource": [
                {
                    "data": {
                        "content": zip_b64,
                        "filetype": "ZIP",
                        "encoding": "BASE64",
                    },
                    "inLineResourceID": f"azure_data_extract_{todays_date}",
                }
            ]
        },
    }
 
    try:
        # Use json=... and keep TLS verification enabled
        resp = requests.post(url, json=body, headers=headers,verify=False, timeout=60)
        if resp.ok:
            logging.info("Email sent successfully. status=%s", resp.status_code)
        else:
            logging.error(
                "Failed to send email. status=%s reason=%s response=%s",
                resp.status_code, resp.reason, resp.text[:2000]
            )
    except requests.RequestException as e:
        logging.exception("Request failed: %s", e)
 
if __name__ == "__main__":
    main()