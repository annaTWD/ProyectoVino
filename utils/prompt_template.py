
def format_prompt(context, query):
    prompt = f"""
    Context:
    {context}

    Query:
    {query}

    Based on the context above, generate a response.
    """
    return prompt
