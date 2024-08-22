clear
echo "Starting Development Server..."
echo "Seting up..."
rm -rf venv > /dev/null
echo "Creating environment..."
python3 -m venv venv > /dev/null
echo "Activating..."
source venv/bin/activate > /dev/null
echo "Updating..."
pip install --upgrade pip > /dev/null
echo "Installing requirements"
pip install -r requirements.txt > /dev/null
echo "Starting Zephyr Nextgen in development mode..."
python backend/backend_view.py > /dev/null
echo "Closing..."
deactivate > /dev/null
echo "Done!"