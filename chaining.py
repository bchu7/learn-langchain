from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate

# instantiation
llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    # other params...
)

# chaining
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm
response = chain.invoke(
    {
        "input_language": "English",
        "output_language": "German",
        "input": "I love programming.",
    }
)

print(response)

''' Response:

content = 'Ich liebe Programmierung.' additional_kwargs = {}
response_metadata = {
    'model': 'llama3.2',
    'created_at': '2025-03-13T14:58:48.9823054Z',
    'done': True,
    'done_reason': 'stop',
    'total_duration': 483752700,
    'load_duration': 17668000,
    'prompt_eval_count': 40,
    'prompt_eval_duration': 202000000,
    'eval_count': 6,
    'eval_duration': 261000000,
    'message': Message(role = 'assistant', content = '', images = None, tool_calls = None)
}
id = 'run-8997d1e2-d1d9-4b2e-8711-5c362ac669e0-0' usage_metadata = {
    'input_tokens': 40,
    'output_tokens': 6,
    'total_tokens': 46
}

'''