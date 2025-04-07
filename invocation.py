from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage

# instantiation
llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    # other params...
)

# invocation
messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
response = llm.invoke(messages)

print(response)

''' response:

content = 'Je aime le programmation.' additional_kwargs = {}
response_metadata = {
    'model': 'llama3.2',
    'created_at': '2025-03-13T14:46:49.2322852Z',
    'done': True,
    'done_reason': 'stop',
    'total_duration': 2858224400,
    'load_duration': 1863704500,
    'prompt_eval_count': 45,
    'prompt_eval_duration': 809000000,
    'eval_count': 7,
    'eval_duration': 182000000,
    'message': Message(role = 'assistant', content = '', images = None, tool_calls = None)
}
id = 'run-a673499a-f733-4a2f-8a1a-6fb31133799f-0' usage_metadata = {
    'input_tokens': 45,
    'output_tokens': 7,
    'total_tokens': 52
}
'''