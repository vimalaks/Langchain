import os
from langchain.chat_models import init_chat_model
#from langchain.schema import HumanMessage,AIMessage
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

# Ensure GROQ_API_KEY is present
if not os.environ.get("GROQ_API_KEY"):
    raise EnvironmentError("GROQ_API_KEY not set in environment variables.")

model = init_chat_model("llama3-8b-8192", model_provider="groq")

# Define the function that calls the model
def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}

# Define a new graph
workflow = StateGraph(state_schema=MessagesState)

# Define the (single) node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "abc123"}}


print("Type exit to end the chat")
while True:
    msg = [HumanMessage(input("Enter your message: "))]
    #if msg.lower() == "exit":
    if msg.lower() == "exit":
        print("No more messages accepted")
        break   

    
    #below is the AI model's response to full conversation history
    ######response = model.invoke(storage)#(msg) #("Hello, World!")    
    response = app.invoke({"messages":msg},config)

    #printing the final response
    #####print("Assistant: ",response.content)
    response["messages"][-1].pretty_print() #response contains all messages in state
