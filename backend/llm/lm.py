from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="tinyllama",
    temperature=0,
)