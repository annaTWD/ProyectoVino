from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_response(context, query):
    model_name = "gpt2"  
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    input_text = f"Context: {context}\n\nQuery: {query}\nAnswer:"
    inputs = tokenizer(input_text, return_tensors="pt")

    outputs = model.generate(inputs["input_ids"], max_length=100, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
