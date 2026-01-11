python3 -m venv venv1
source venv1/bin/activate
pip install -r requirements.txt
# pip freeze : lists all the packages with their versions installed in the current virtual environment
pip freeze > requirements.txt
# pip install -r requirements.txt --trusted-host <hostname_1> --trusted-host <hostname_2>
# pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org pip <package name>

deactivate

python3 -m venv venv2
source venv2/bin/activate
pip install -r dev-requirements.txt
deactivate

 
echo "Setup complete. Two virtual environments created: venv1 and venv2."
#!/bin/bash

# Create the first virtual environment and install production dependencies
python3 -m venv venv1
source venv1/bin/activate
pip install -r requirements.txt
deactivate

# Create the second virtual environment and install development dependencies
python3 -m venv venv2
source venv2/bin/activate
pip install -r dev-requirements.txt
deactivate

echo "Setup complete. Two virtual environments created: venv1 and venv2."

