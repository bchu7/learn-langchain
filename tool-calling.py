# first pull the model by run command: ollama pull llama3.2

from typing import List

from langchain_core.tools import tool
from langchain_ollama import ChatOllama

# agent?
@tool
def validate_user(user_id: int, addresses: List[str]) -> bool:
    """Validate user using historical addresses.

    Args:
        user_id (int): the user ID.
        addresses (List[str]): Previous addresses as a list of strings.
    """
    return True


llm = ChatOllama(
    model="llama3.2",
    temperature=0,
).bind_tools([validate_user])

result = llm.invoke(
    "Could you validate user 123? They previously lived at "
    "123 Fake St in Boston MA and 234 Pretend Boulevard in "
    "Houston TX."
)

print(result.tool_calls)

''' Response:

[{
    'name': 'validate_user',
    'args': {
        'addresses': ['123 Fake St', '234 Pretend Boulevard'],
        'user_id': 123
    },
    'id': '7a55bd89-8011-402b-aec8-316d1ab1b577',
    'type': 'tool_call'
}]

'''