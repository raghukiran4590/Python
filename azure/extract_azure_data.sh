#!/bin/zsh
echo "Running PowerShell script..."
pwsh -NoProfile -ExecutionPolicy Bypass -File "./azure_data_extract.ps1"
echo "PowerShell script finished."
echo "Starting the Python script..."
python3 "./send_email.py"
echo "Python script finished."


