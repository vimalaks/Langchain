import os
from langchain.chat_models import init_chat_model
from langchain.schema import HumanMessage,AIMessage

# Ensure GROQ_API_KEY is present
if not os.environ.get("GROQ_API_KEY"):
    raise EnvironmentError("GROQ_API_KEY not set in environment variables.")

model = init_chat_model("llama3-8b-8192", model_provider="groq")
#context aware code start
#Store the conversation history
storage = []
#context aware code end
print("Type exit to end the chat")
while True:
    msg = input("Enter your message: ")
    if msg.lower() == "exit":
        print("No more messages accepted")
        break

    #context aware code start
    #append user message in storage
    storage.append(HumanMessage(content = msg))
    #context aware code end

    #below is the AI model's response to full conversation history
    response = model.invoke(storage)#(msg) #("Hello, World!")

    #context aware code start
    #append AI model's reponse in storage
    storage.append(AIMessage(content = response.content))
    #context aware code end

    #printing the final response
    print("Assistant: ",response.content)