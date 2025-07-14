from data import graphContext
from utils import azure_openai_model
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers.json import JsonOutputParser

def summarize_sentiment_node(state: graphContext) -> graphContext:
    
    prompt = """
                Summarize the sentiment of these messages and classify as 'positive', 'negative', or 'neutral':\n"
                User Reviews: {user_review}\n

                Please output your response as a JSON object like this:
                {{
                    "sentiment": positive/negative/neutral,
                    "explanation": "The ticket has captured this..."
                }}
            """
    output_parser = JsonOutputParser()

    llm = azure_openai_model(temperature=0.0)
    chain_prompt = PromptTemplate(
            template=prompt, input_variables=['user_review']
        )
    llm_prompt_chain = chain_prompt | llm | output_parser
    response = llm_prompt_chain.invoke({'user_review':state['cleaned_messages']})


    state["sentiment_summary"] = response.get("explanation", "No explanation provided.")
    state["sentiment_class"] = response.get("sentiment", "neutral")
    return state