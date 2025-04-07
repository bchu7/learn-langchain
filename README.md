# langchain with ollama example
https://python.langchain.com/docs/integrations/chat/ollama/

## prerequisites
- install ollama and pull models:
  - https://ollama.com/
  - ollama pull llama3.2
  - ollama pull gemma3:4b
- install langchain packages:
  - pip install -U langchain-ollama langchain-core pillow
  - pip install -U ipython

---
### LLM.invoke()
```py invocation.py```

### LLM.invoke() by chaining prompt | LLM
```py chaining.py```

### LLM.invoke() with custom agent/validator
```py tool-calling.py```
### Load and display the image sample.png on the browser, then describe the image using a LLM
```py multi-modal.py```
