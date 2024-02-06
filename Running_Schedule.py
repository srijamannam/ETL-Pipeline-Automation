import schedule
import time
import subprocess


def run_main_script():
    # Replace 'your_script.py' with the actual path to your main script.
    script_path = 'C:\\Users\\danie\\PycharmProjects\\pythonProject\\scrap_and_transform.py'

    # Replace 'python' with the full path to the Python interpreter within your virtual environment.
    python_path = 'C:\\Users\\danie\\PycharmProjects\\pythonProject\\venv\\Scripts\\python.exe'

    subprocess.run([python_path, script_path])

def run_csv_to_db_script():
    script_path = 'C:\\Users\\danie\\PycharmProjects\\pythonProject\\csv_to_db.py'
    python_path = 'C:\\Users\\danie\\PycharmProjects\\pythonProject\\venv\\Scripts\\python.exe'

    subprocess.run([python_path, script_path])

# Schedule run_main_script.
schedule.every().day.at("10:01").do(run_main_script)


# Schedule run_csv_to_db_script
schedule.every().day.at("10:01").do(run_csv_to_db_script)

while True:
    schedule.run_pending()
    time.sleep(1)

