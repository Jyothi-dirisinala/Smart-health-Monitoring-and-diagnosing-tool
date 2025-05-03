Smart Health Monitoring System
 Overview
 
 The Smart Health Monitoring System is a desktop application designed to help manage and
 analyze patient health data. It provides a graphical user interface (GUI) built with Tkinter to
 load patient records from a CSV file, calculate health risk levels based on vital signs (Blood
 Pressure, Glucose, BMI), and display insights through a dashboard, visualizations, and
 personalized advice. The system aims to offer a user-friendly way to monitor patient status
 and identify individuals requiring attention.
 
 Features 
 
 -Data Loading: Load patient health data from CSV files.
 
 -Patient Records Display: View patient data (Name, Age, Blood Pressure, Glucose,
 BMI, Risk Level) in a sortable and filterable table.
 
 -Risk Analysis: Automatically calculates a risk level (Critical, High, Moderate,
 Normal) for each patient based on their vital signs using predefined rules.
 
 -BMI Calculation: Calculates the Body Mass Index (BMI) category (Underweight,
 Normal, Overweight, Obese) for each patient.
 
 -Dashboard Overview: Displays summary statistics, including the total number of
 patients and counts for each risk level.
 
 -Risk Distribution Visualization: Presents a bar chart showing the distribution of
 patients across different risk levels.
 
 -Health Advice: Provides tailored recommendations based on the selected
 patient’s calculated risk level.
 
 -Search and Filter: Search for patients by name and filter the patient list by risk
 level.
 
 -Data Saving: Save the current patient data (potentially with updates, although
 direct editing isn’t implemented) back to the loaded CSV file.
 
 -Report Exporting: Export a summary report (details need confirmation based on 
  export_report implementation).
  
 -Q&A Assistant: A simple feature to answer basic, general health-related questions.
 
 -Tooltips: Provides helpful hints for certain UI elements.
 
Project Structure

The project is organized into several Python modules:
-main.py : The main entry point to launch the application.
 src/__init__.py : Makes the src directory a Python package.
 
 -src/gui/main_window.py : Defines the main HealthApp class, responsible
 for building and managing the Tkinter GUI, including all widgets, layouts, and
 event handling.
 
 -src/gui/tooltip.py : Provides a helper class to create tooltips for GUI
 widgets.
 
 -src/data_handler.py : Contains the for reading patient data from CSV files.
 
 -src/patient.py : Defines the DataManager class with static methods Patient class, which serves as the data modelfor individual patients, including BMI calculation logic.
 
 -src/stats.py : Contains the RiskAnalyzer class with static methods for calculating the health risk level for a patient.
 
 -patients_data.csv : A sample CSV file containing patient data in the expected format.
 
 -test_patient.py , 
 -test_stats.py : Unit tests for the RiskAnalyzer classes respectively.
 
 Setup and Installation
 
1.Patient and Prerequisites: Ensure you have Python 3 installed on your system. The application
also uses Tkinter for its graphical interface, which is typically included with standard Python installations (though on some Linux systems, you might need toinstall a package like python3-tk ).
2.Clone the Repository (if applicable): If the code is in a Git repository, clone it to your local machine.
3.Install Dependencies: The application requires the libraries. Install them using pip: bash     pip install pandas matplotlib
4.File Placement: Ensure all the Python files (contents) and the pandas and main.py , matplotlibsrc/ directory and its patients_data.csv file are placed correctly according to theproject structure described above.
 
 Usage
 
1.Run the Application: Navigate to the project’s root directory in your terminal
 and run: bash     python main.py Alternatively, if your structure differs, you might need to run python src/gui/main_window.py directly, ensuring
 Python can find the other modules.
 
2.Load Data: Click the “📂 Load” button and select a CSV file containing patient
 data (like the provided patients_data.csv ). The table, dashboard, and
 visualization will update.
 -View Patient Records: The main table displays the loaded patient records. You
 can:
 -Sort: Click on any column header (Name, Age, BP, etc.) to sort the table
 by that column. Click again to reverse the sort order.
 -Select: Click on a patient row to view their specific details and health
 advice in the right-hand panels.
 
 3.Search and Filter: Use the “Search” entry box to type parts of a patient’s name. The table will update automatically as you type.
 -Use the “Filter Risk” dropdown to select a specific risk level(“Critical”, “High”, “Moderate”, “Normal”) or “All” to viewpatients matching that risk level.
 
 4.Dashboard: The “Dashboard Overview” panel shows real-time counts of total patients and patients in each risk category.
 
 5.Visualization: The “Risk Distribution” panel displays a bar chart visualizing the number of patients in each risk category.
 
 6.Health Advice: When a patient is selected in the table, the “Patient Health Advice” panel shows their details (including BMI category) and provides general
 recommendations based on their risk level.
 
 7.Q&A Assistant: Type a general health question (e.g., “bmi ranges”, “normal blood pressure”) into the “Health Q&A Assistant” entry box and click “Ask
 Question ➔” to get a predefined basic answer.
 
 8.Save Data: Click the “💾 Save” button to save the current list of patients back tothe originally loaded CSV file. Note: This overwrites the original file.
 
 9.Export Report: Click the “📊 Export” button to generate and save a report (likely PDF format, based on imports in choose a save location.
 main_window.py ). You will be prompted to choose a save location
 
Data Format

The application expects input data in a CSV file with the following columns:

 name : Patient’s full name (string).
 age : Patient’s age in years (integer).
 blood_pressure : Patient’s blood pressure reading as “Systolic/
 Diastolic” (string, e.g., “120/80”).
 glucose : Patient’s blood glucose level (float/integer, e.g., 95.5).
 bmi : Patient’s Body Mass Index (float, e.g., 22.7).
 patients_data.csv row:
 
 Example patients_data.csv row:
 name,age,blood_pressure,glucose,bmi
 John Smith,55,135/88,170,28.5
 
 Testing
 
 The project includes unit tests for core logic:
 
test_patient.py : Tests the Patient class functionality (e.g., BMI calculation).
test_stats.py : Tests the  RiskAnalyzer class functionality (e.g., risk level calculation).
 
 
 To run the tests, navigate to the project’s root directory (or the directory containing the
 test files) and use Python’s unitest module:
 python -m unittest test_patient.py
 python -m unittest test_stats.py
 
Authors
Gracious Regina Zigara
Jyothi
