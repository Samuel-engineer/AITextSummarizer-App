def summarize_text(text, tokenizer, model, max_length=1024):
    input_ids = tokenizer(text, return_tensors="pt").input_ids
    output = model.generate(
        input_ids,
        max_length=max_length,
        num_beams=5,
        early_stopping=True
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)
