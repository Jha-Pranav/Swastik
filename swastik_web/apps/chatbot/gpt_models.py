# from transformers import AutoTokenizer, AutoModelForCausalLM

# tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6b")

# model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6b")

# def generate_response(prompt):
#     # Tokenize the prompt and convert to tensor
#     input_ids = tokenizer.encode(prompt, return_tensors="pt")
#     # Generate text from the model
#     output = model.generate(input_ids, max_length=1000, do_sample=True)
#     # Decode the generated text and return
#     response = tokenizer.decode(output[0], skip_special_tokens=True)
#     return response

# print(generate_response('How are you ?'))
