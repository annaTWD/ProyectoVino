from langchain.prompts import PromptTemplate

def get_prompt_template():
    """
    Define el prompt para extraer información de una factura o documento.
    
    Returns:
        PromptTemplate: La plantilla del prompt lista para ser utilizada.
    """
    prompt_template = PromptTemplate(
        input_variables=["text"],
        template="""
        Por favor, extrae la siguiente información del manual de manera estructurada:
        
        Manual:
        {text}

        Respuesta:
        """
    )
    return prompt_template