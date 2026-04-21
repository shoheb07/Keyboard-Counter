# Keyboard-Counter
A keyboard counter in Python typically tracks how many times keys are pressed. This can be done using the keyboard library.

⌨️ Keyboard Counter in Python

📌 Description

The Keyboard Counter is a Python program that tracks and counts key presses made by the user. It can:

- Count total number of key presses
- Track how many times each individual key is pressed
- Stop execution when a specific key (e.g., "ESC") is pressed

This project demonstrates basic event handling and real-time input tracking in Python.


🚀 Features

- Real-time key press detection
- Total key press counter
- Individual key tracking (key-wise count)
- Stop program using a predefined key ("ESC")
- Simple and easy-to-understand implementation


🛠️ Technologies Used

- Python 3
- "keyboard" library (for capturing key events)


📦 Installation

1. Install Python (if not already installed)
2. Install the required library:
   pip install keyboard


▶️ How to Run

1. Save the Python file (e.g., "keyboard_counter.py")
2. Open terminal/command prompt
3. Run the script:
   python keyboard_counter.py


⚠️ Important Notes

- Run the program as Administrator (Windows) or with sudo (Linux) for proper key detection
- Some IDEs (like IDLE) may not support global keyboard input
- Works best in terminal/command prompt


📊 Example Output

Press any key... Press 'esc' to stop.
Key pressed: a | Total count: 1
Key pressed: b | Total count: 2
Key pressed: a | Total count: 3

Stopped!
Total key presses: 3


📂 Project Structure

keyboard-counter/
│── keyboard_counter.py
│── README.md


🔮 Future Improvements

- Add GUI using Tkinter
- Create typing speed tester
- Save results to a file
- Display statistics (most used key, etc.)


👨‍💻 Author

Developed as a simple Python project for learning keyboard event handling.
