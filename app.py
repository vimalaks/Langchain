import os
from langchain.chat_models import init_chat_model

# Ensure GROQ_API_KEY is present
if not os.environ.get("GROQ_API_KEY"):
    raise EnvironmentError("GROQ_API_KEY not set in environment variables.")

model = init_chat_model("llama3-8b-8192", model_provider="groq")

response = model.invoke("Hello, World!")
print(response)