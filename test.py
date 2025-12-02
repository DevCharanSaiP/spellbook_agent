import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# 1. Load token from .env
load_dotenv()
token = os.getenv("HUGGINGFACE_API_TOKEN")

# 2. Create client with a chat model
client = InferenceClient(
    "meta-llama/Meta-Llama-3-8B-Instruct",  # or "mistralai/Mistral-7B-Instruct-v0.3"
    token=token,
)

# 3. Use chat_completion (NOT text_generation)
messages = [
    {"role": "user", "content": "Create a simple fire spell name only."}
]

response = client.chat_completion(
    messages=messages,
    max_tokens=50,
    temperature=0.9,
)

print("✅ Connection successful!")
print("Test spell name:", response.choices[0].message["content"])