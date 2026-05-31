from langchain_core.prompts import PromptTemplate
from app.llms.gemini_llm import llm

prompt = PromptTemplate(
    template="""
You are a helpful AI assistant.

Answer ONLY from the provided context.

If context is insufficient,
say "I don't know."

Context:
{context}

Question:
{question}
""",
    input_variables=["context", "question"]
)

def generate_answer(context, question):

    final_prompt = prompt.invoke(
        {
            "context": context,
            "question": question
        }
    )

    response = llm.invoke(final_prompt)

    return response.content