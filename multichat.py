import tkinter as tk
from tkinter import scrolledtext
import requests

API_URL_1 = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
API_URL_2 = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
API_URL_3 = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
API_URL_4 = "https://api-inference.huggingface.co/models/google/gemma-7b"
API_URL_5 = "https://api-inference.huggingface.co/models/openai-community/gpt2"
API_URL_6 = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"

headers = {"Authorization": "Bearer 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"}

def query(api_url, payload):
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error querying API: {response.text}")
        return None

def generate_response():
    # Pre-prompt for the final model
    prePrompt = """
                Based on the insights and perspectives shared by the other models, 
                please synthesize a comprehensive and cohesive response that 
                addresses the user's input in the most informative and engaging 
                manner possible.
                """
    
    # Pre-prompt specifically for the first five models
    pre_prompt_first_five = """
                             You are generating responses for a final model to use for a
                             final response. Please provide a response to the following user input
                             that is informative and will allow the final model to generate a 
                             cohesive and comprehensive response.
                             """

    # Get user input from the text field                         
    user_input = user_input_text.get("1.0", tk.END).strip()
    
    # Generate response from the first model
    response1 = query(API_URL_1, {"inputs": pre_prompt_first_five + "\n\n" + user_input})
    generated_text_1 = response1[0]["generated_text"]
    
    # Use the response from the first model as input for the second model
    response2 = query(API_URL_2, {"inputs": pre_prompt_first_five + "\n\n" + user_input})
    generated_text_2 = response2[0]["generated_text"]

    # Use the response from the first model as input for the second model
    response3 = query(API_URL_3, {"inputs": pre_prompt_first_five + "\n\n" + user_input})    
    generated_text_3 = response3[0]["generated_text"]

    # Use the response from the first model as input for the second model
    response4 = query(API_URL_4, {"inputs": pre_prompt_first_five + "\n\n" + user_input})
    generated_text_4 = response4[0]["generated_text"]

    # Use the response from the first model as input for the second model
    response5 = query(API_URL_5, {"inputs": pre_prompt_first_five + "\n\n" + user_input})
    generated_text_5 = response5[0]["generated_text"]

    # Use the response from the other models as input for this model
    finalAnswer = query(API_URL_6, {"inputs": " ".join([prePrompt, "and", user_input, "and", generated_text_1, "and", generated_text_2,
                                                        "and", generated_text_3, "and", generated_text_4, "and", generated_text_5])})

    generated_text_6 = finalAnswer[0]["generated_text"]
    
    # Output the response from the third model to the user
    bot_output_text.insert(tk.END, "Bot: " + generated_text_6 + "\n")

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
