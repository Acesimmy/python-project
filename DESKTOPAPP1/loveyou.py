import time
import sys
import itertools

# Define the message
message = "Love you, Sandeep! 💖\nPython loves you too! 🐍"

# Animation function
def typing_animation(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after typing

# Heartbeat animation
def heartbeat_animation():
    heart_frames = ["💓", "💗", "💖", "💗", "💓"]
    for _ in range(10):  # Loop for a few beats
        for frame in heart_frames:
            sys.stdout.write(f"\r{frame} Love you, Sandeep!")
            sys.stdout.flush()
            time.sleep(0.2)
    print("\r" + " " * 30, end="")  # Clear line

# Main animation
if __name__ == "__main__":
    typing_animation("Initializing...\n", delay=0.05)
    typing_animation(message, delay=0.1)
    heartbeat_animation()
    print("\nThank you for being awesome! 💻🐍")
