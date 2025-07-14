from data import graphContext, graphOutput
from utils import azure_openai_model
from langchain.prompts import PromptTemplate


def generate_response_node(state: graphContext) -> graphOutput:

    prompt = """
                Write a polite customer response based on this summary:\n'{sentiment_summary}'\n
                User Review: {user_review}\n
                The response should be concise, empathetic, and address the user's concerns.
                Ensure the response is professional and suitable for customer service communication.
                Don't write it as an email, just the response text.
            """    

    llm = azure_openai_model(temperature=0.0)
    chain_prompt = PromptTemplate(
            template=prompt, input_variables=['sentiment_summary','user_review']
        )
    llm_prompt_chain = chain_prompt | llm 

    
    response = llm_prompt_chain.invoke({'sentiment_summary': state['sentiment_summary'],
        'user_review': state['cleaned_messages']}).content

    return {
        "id": state["id"],
        "sentiment_summary": f"{state['sentiment_summary']}\n\nResponse: {response}"
    }
