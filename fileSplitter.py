#SPLITS FILES
import os
import glob
from transformers import AutoTokenizer

def tokenize(text, tokenizer):
    return tokenizer.tokenize(text)

def split_text_file(file_path, max_tokens=2000, tokenizer_name_or_path='gpt2'):
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name_or_path)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    tokens = tokenize(text, tokenizer)
    num_parts = (len(tokens) + max_tokens - 1) // max_tokens
    
    for i in range(num_parts):
        start = i * max_tokens
        end = min((i + 1) * max_tokens, len(tokens))
        chunk_tokens = tokens[start:end]
        chunk_text = tokenizer.convert_tokens_to_string(chunk_tokens)
        
        output_file = f"{os.path.splitext(file_path)[0]}_part{i + 1}.txt"
        with open(output_file, 'w', encoding='utf-8') as out_file:
            out_file.write(chunk_text)

def main():
    search_path = '**/*.txt'
    text_files = glob.glob(search_path, recursive=True)
    
    for file_path in text_files:
        split_text_file(file_path)

if __name__ == '__main__':
    main()
