from flask import Flask, jsonify
import threading
import time
import random

app = Flask(__name__)

# List of random texts
texts = [
    "Keep going, you're doing great!",
    "Success is a journey, not a destination.",
    "Dream big and dare to fail.",
    "Consistency is key to success.",
    "Believe in yourself and all that you are.",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones."
]

# Variable to hold the current random text
current_text = {"text": "Server is starting..."}

def update_random_text():
    global current_text
    while True:
        # Pick a random text
        current_text["text"] = random.choice(texts)
        print(current_text["text"])  # Log to the console
        # Wait for 30 seconds
        time.sleep(30)

@app.route("/", methods=["GET"])
def get_random_text():
    # Return the current random text
    return jsonify(current_text)

if __name__ == "__main__":
    # Start the background thread for updating texts
    threading.Thread(target=update_random_text, daemon=True).start()
    # Run the server on port 3000
    app.run(host="0.0.0.0", port=3000)
