# Command-Line Pomodoro Timer

#### Video Demo: https://youtu.be/ffnTKm2E7aw?si=JEKxlWHlyNg7eHtk

#### Description:
This is the final project for Harvard's CS50's Introduction to Programming with Python (CS50P). This project is a command-line Pomodoro Timer application, written entirely in Python.

The Pomodoro Technique is a popular time management method that uses a timer to break work into focused intervals, separated by short breaks. This application automates the process, freeing the user from manually setting timers. It provides both visual and audio notifications when a session ends, ensuring users adhere to their work/break schedule effectively.

---

## Features

* **Countdown Timer:** Displays the remaining time in a `MM:SS` format, updating every second on a single, non-wrapping line.
* **Customizable Timers:** Users can easily set custom durations for work sessions, short breaks, and long breaks via command-line arguments.
* **Automatic Cycling:** The program automatically cycles between work and break sessions. After four work sessions, a long break is initiated.
* **Audio-Visual Notifications:** Upon the completion of each session, the application alerts the user with a clear message on the terminal and a distinct audio notification.
* **Input Validation:** The program validates user input to prevent non-positive time values, exiting with a clear error message if the input is invalid.
* **Graceful Exit:** Users can smoothly exit the application at any time by pressing `Ctrl+C`.

---

## Installation & Usage

To run this project on your local machine, please follow these steps:

#### 1. Set up the Environment
First, clone this repository (or download the source code). Then, open a terminal in the project's root directory and create a virtual environment:
```bash
python -m venv venv
```
Activate the virtual environment:
* On Windows: `.\venv\Scripts\activate`
* On macOS/Linux: `source venv/bin/activate`

#### 2. Install Dependencies
This project relies on a few external libraries. Install them using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

#### 3. Run the Program
You can run the program with the default settings (25-minute work, 5-minute short break):
```bash
python project.py
```
Or, you can provide custom durations using the `-w` (work), `-s` (short break), and `-l` (long break) arguments:
```bash
python project.py -w 45 -s 10 -l 30
```
The application also accepts float values for quick testing (e.g., `0.5` for 30 seconds):
```bash
python project.py -w 0.5 -s 0.1
```
To stop the program at any time, press `Ctrl+C`.

---

## Project Structure & Design Choices

The project is intentionally structured to promote clarity, maintainability, and testability.

* `project.py`: This is the main file containing all the application logic.
    * **`main()`**: The primary function that orchestrates the application's main work/break loop.
    * **`get_args()`**: Uses Python's `argparse` library to parse command-line arguments. I chose `argparse` for its robustness, flexibility, and automatic generation of helpful user-facing messages.
    * **`count_down()`**: The core function responsible for the countdown logic and display.
    * **`format_time()` & `valid_time()`**: These are helper functions refactored from the main logic. `format_time` handles the `MM:SS` string formatting, while `valid_time` ensures all time inputs are valid. Separating this logic into smaller, pure functions makes testing significantly easier and more reliable.
    * **`notify_user()` & `category_message()`**: These functions manage user notifications. The logic is decoupled to make it easy to change notification messages or methods in the future.

* `test_project.py`: This file contains all the tests for the project, written using the `pytest` framework.
* `requirements.txt`: Lists the external Python libraries required by the project (i.e., `playsound`).
* Audio Files (`lofi.mp3`, `warning.mp3`): Sound files used for notifications.

---

## Testing

I have written a suite of tests to ensure the core logical components of the application function correctly.

* `test_valid_time()`: This test asserts that the function correctly accepts positive time values and raises a `ValueError` for non-positive inputs (zero or negative numbers).
* `test_format_time()`: This test checks that the function accurately converts a given number of seconds into the `MM:SS` string format under various conditions (e.g., 0 seconds, 59 seconds, 60 seconds).
* `test_category_message()`: This test verifies that the message categorization logic correctly returns `True` or `False` based on the message content, ensuring the right notification style is applied.

To run the tests, execute the following command in the terminal:
```bash
pytest
```