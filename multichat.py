import tkinter as tk
from tkinter import scrolledtext
import requests

API_URLS = [
    "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2",
    "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct",
    "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1",
    "https://api-inference.huggingface.co/models/google/gemma-7b",
]

headers = {"Authorization": "Bearer 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"}

def query(api_url, payload):
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error querying API: {response.text}")
        return None

def generate_response():
    # Get user input from the text field
    user_input = user_input_text.get("1.0", tk.END).strip()

    # Initialize the response
    response = user_input

    # Refine the response iteratively
    for i in range(5):  # refine 5 times
        # Add additional context to the input
        input_text = f"Refine the following response to create the most accurate and informative: {response}"
        api_url = API_URLS[i % len(API_URLS)]  # cycle through the API URLs
        response_json = query(api_url, {"inputs": input_text})
        print(response_json)
        generated_text = response_json[0]["generated_text"]

        # Update the response
        response = generated_text

    # Output the refined response from the model to the user
    bot_output_text.insert(tk.END, "Bot: " + response + "\n\n")



# Create main window
root = tk.Tk()
root.title("Chat Bot")

# Create text input field
user_input_label = tk.Label(root, text="You:")
user_input_label.pack()
user_input_frame = tk.Frame(root)
user_input_frame.pack(fill=tk.BOTH, expand=True)
user_input_text = scrolledtext.ScrolledText(user_input_frame, width=50, height=10)
user_input_text.pack(fill=tk.BOTH, expand=True)

# Create button to generate response
generate_button = tk.Button(root, text="Generate Response", command=generate_response)
generate_button.pack()

# Create text output field
bot_output_label = tk.Label(root, text="Bot:")
bot_output_label.pack()
bot_output_frame = tk.Frame(root)
bot_output_frame.pack(fill=tk.BOTH, expand=True)
bot_output_text = scrolledtext.ScrolledText(bot_output_frame, width=50, height=10)
bot_output_text.pack(fill=tk.BOTH, expand=True)

# Start the GUI event loop
root.mainloop()
