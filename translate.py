import sys
from googletrans import Translator

def translate_text(text, src_language='fr', dest_language='en'):
    translator = Translator()
    try:
        translated = translator.translate(text, src=src_language, dest=dest_language)
        return translated.text
    except Exception as e:
        print(f"Translation error: {e}")
        return text

def translate_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        translated_content = translate_text(file_content)
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(translated_content)
        print(f"Translated content saved to {output_file_path}")
    except Exception as e:
        print(f"File processing error: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python translate_extension.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    translate_file(input_file_path, output_file_path)

if __name__ == "__main__":
    main()