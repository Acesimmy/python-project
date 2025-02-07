import time
import os

# Define the message
message = "❤️ Love you Sandeep ❤️    Love Python ❤️"
message = " " * 20 + message + " " * 20  # Add some spacing for smoother scrolling

# Define the display function
def scroll_text(text):
    while True:
        os.system("cls" if os.name == "nt" else "clear")  # Clear screen
        print(text)
        text = text[1:] + text[0]  # Rotate the text
        time.sleep(0.1)

# Run the animation
try:
    scroll_text(message)
except KeyboardInterrupt:
    print("\nAnimation stopped!")
