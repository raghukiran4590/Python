# Define email properties
$RecipientEmail = "raghu.kiran@elevancehealth.com"
$Subject = "Automated Email with Attachment"
$Body = "Hi there, please see the attached file."
$AttachmentPath = "/azure/azure_resource_data_2026_03_16.zip"

# Create an Outlook Application object
$Outlook = New-Object -ComObject Outlook.Application
$Mail = $Outlook.CreateItem(0) # 0 = olMailItem

# Set email properties
$Mail.To = $RecipientEmail
$Mail.Subject = $Subject
$Mail.Body = $Body

# Attach the file
$Mail.Attachments.Add($AttachmentPath)

# Send the email (use $Mail.Display() to open it for review before sending)
$Mail.Send()

# Clean up the Outlook object (optional but good practice)
# [System.Runtime.InteropServices.Marshal]::ReleaseComObject($Mail) | Out-Null
# [System.Runtime.InteropServices.Marshal]::ReleaseComObject($Outlook) | Out-Null

# powershell -ExecutionPolicy Bypass -File /azure/Send-OutlookMail.ps1
