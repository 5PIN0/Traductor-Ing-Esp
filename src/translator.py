from transformers import MarianMTModel, MarianTokenizer

def load_model():
    model_name = 'Helsinki-NLP/opus-mt-en-es'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    return model, tokenizer

def translate_text(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(inputs['input_ids'], max_length=100)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text