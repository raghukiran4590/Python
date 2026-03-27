# Requires TLS 1.2 for secure connection with Office 365
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12

# Define credentials (prompt for security or use a secure string)
$credential = Get-Credential 

# Email properties
$EmailFrom = "raghu.kiran@elevancehealth.com"
$EmailTo = "raghu.kiran@elevancehealth.com"
$Subject = "Test Email from PowerShell"
$Body = "This is a test email sent from a PowerShell script using Office 365 SMTP."
$SMTPServer = "outlook.office365.com"
$Port = 587

# Send the email
# Send-MailMessage -From $EmailFrom -To $EmailTo -Subject $Subject -Body $Body -SmtpServer $SMTPServer -Port $Port -UseSsl -Credential $credential

Send-MailMessage -From $EmailFrom -To $EmailTo -Subject $Subject -Body $Body -SmtpServer $SMTPServer -Port $Port -Credential $credential

Write-Host "Email sent successfully!"
