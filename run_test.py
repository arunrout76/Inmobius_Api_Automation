import subprocess
import os

def run_behave_tests():
    try:
        print("Tarun")
        # Activate the virtual environment
        venv_python = os.path.join('venv', 'Scripts', 'python.exe')

        # Run Behave tests with Allure formatter
        subprocess.run([
            venv_python,
            '-m', 'behave',
            '-f', 'allure_behave.formatter:AllureFormatter',
            '-o', './Reports/Allure_Result',
            './features/student_register.feature'
        ], check=True)

        # Generate Allure report
        subprocess.run([
            venv_python, '-m', 'allure', 'generate',
            './Reports/Allure_Result',
            '-o', './Reports/Allure_Report',
            '--clean'
        ], check=True)

        # Send email with the report
        subprocess.run([venv_python, './utility/send_mail.py'], check=True)

        print("All commands executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    run_behave_tests()
