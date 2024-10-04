from utils.data_loader import load_data, search_data
from models.model2 import generate_response
from utils.prompt_template import format_prompt

def main():
    df = load_data("data/skills.csv")

    query = input("Introduce tu consulta: ")

    results = search_data(df, query)
    
    if not results.empty:
        
        context = results.to_string()

      
        prompt = format_prompt(context, query)

      
        response = generate_response(context, query)

        print("Respuesta Generada:\n", response)
    else:
        print("No se encontraron resultados relevantes en los datos.")

if __name__ == "__main__":
    main()
