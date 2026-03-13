        ---
        name: langchain-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/langchain-expert/SKILL.md
        description: Build LangChain pipelines: chains, agents, memory, and LCEL patterns.
        ---

        You build reliable LangChain pipelines with LCEL.

## LCEL Chain Pattern
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-opus-4-6")
prompt = ChatPromptTemplate.from_template("Summarize: {text}")

# LCEL chain
chain = prompt | llm | StrOutputParser()

# With streaming
for chunk in chain.stream({"text": long_document}):
    print(chunk, end="", flush=True)

# With structured output
from langchain_core.output_parsers import JsonOutputParser
json_chain = prompt | llm | JsonOutputParser()
```

## Rules
- LCEL (pipe syntax) over legacy `LLMChain` class.
- Use `RunnableParallel` for concurrent independent calls.
- Always set timeouts — LLM calls can hang.
- Use callbacks for logging and monitoring, not manual print statements.
