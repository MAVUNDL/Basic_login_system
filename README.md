# 🚀 Python GUI Application
![Screenshot (14)](https://github.com/MAVUNDL/Basic_login_system/assets/117544413/d1233a83-4ad4-41ad-b4c9-943b8c4e523e)


This application is a GUI (Graphical User Interface) built with Python. It uses the `customtkinter` library to create a user-friendly interface for user authentication (login and sign-up).

## 📂 File Structure

The application consists of three main Python files:

1. `FunctionsMODULE.py`
2. `savingdata.py`
3. `Main.py`

### 🖼️ FunctionsMODULE.py

This file contains several functions that are used to create the login and sign-up interface. It includes functions to create frames, switch between frames, and place widgets in the frames.

### 💾 savingdata.py

This file is responsible for interacting with a SQLite database to store and validate user credentials. It includes functions to save user information to the database and retrieve information from the database for validation.

### 🎯 Main.py

This is the main file that runs the application. It imports the necessary functions from `FunctionsMODULE.py`, creates the application window, and initializes the login and sign-up frames.

## 🏃‍♀️ How to Run the Application

To run this application, you need to have Python installed on your system along with the `customtkinter` and `PIL` libraries. You can install these libraries using pip:

```bash
pip install customtkinter pillow
