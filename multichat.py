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


prePrompt = "choose the single best response: "

# Main chat loop
while True:
    user_input = input("You: ")
    
    # Generate response from the first model
    response1 = query(API_URL_1, {"inputs": user_input})
    generated_text_1 = response1[0]["generated_text"]
    #print("Response from model 1:", response1)
    
    # Use the response from the first model as input for the second model
    response2 = query(API_URL_2, {"inputs": user_input})
    generated_text_2 = response2[0]["generated_text"]
    #print("Response from model 2:", response2)

    # Use the response from the first model as input for the second model
    response3 = query(API_URL_3, {"inputs": user_input})    
    generated_text_3 = response3[0]["generated_text"]
    #print("Response from model 3:", response3)

    # Use the response from the first model as input for the second model
    response4 = query(API_URL_4, {"inputs": user_input})
    generated_text_4 = response4[0]["generated_text"]
    #print("Response from model 4:", response4)

    # Use the response from the first model as input for the second model
    response5 = query(API_URL_5, {"inputs": user_input})
    generated_text_5 = response5[0]["generated_text"]
    #print("Response from model 5:", response5)

    # Use the response from the other models as input for this model
    finalAnswer = query(API_URL_6, {"inputs": " ".join([prePrompt, generated_text_1, "and", generated_text_2,
                                                    "and", generated_text_3, "and", generated_text_4,
                                                    "and", generated_text_5])})

    generated_text_6 = finalAnswer[0]["generated_text"]
    
    # Output the response from the third model to the user
    print("Bot:", generated_text_6)
