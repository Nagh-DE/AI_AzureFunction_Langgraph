from langchain_openai import AzureChatOpenAI

def azure_openai_model(deployment_name: str, temperature: float = 0.0) -> AzureChatOpenAI:
    llm = AzureChatOpenAI(deployment_name=deployment_name, temperature=temperature)

    return llm