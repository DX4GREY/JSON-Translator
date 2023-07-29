import json
import time
import sys
import argparse
from loading import LoadingThread
from googletrans import Translator


def translate_json_value(value, translator):
    # Menerjemahkan nilai JSON
    if isinstance(value, str):
        return translator.translate(value, dest=json_lang_dest).text
    elif isinstance(value, list):
        translated_list = []
        for item in value:
            translated_item = translate_json_value(item, translator)
            translated_list.append(translated_item)
        return translated_list
    elif isinstance(value, dict):
        translated_dict = {}
        for key, val in value.items():
            translated_key = translate_json_value(key, translator)
            translated_val = translate_json_value(val, translator)
            translated_dict[translated_key] = translated_val
        return translated_dict
    else:
        return value


def translate_json_file(file_path):
    # Membaca data JSON dari file
    with open(file_path, 'r') as file:
        json_data = json.load(file)

    # Menerjemahkan nilai JSON
    translator = Translator()
    total_keys = len(json_data)
    loading = LoadingThread("[*] Translating", 'horizontal')
    loading.start()
    for i, key in enumerate(json_data.keys()):
        value = json_data[key]
        translated_value = translate_json_value(value, translator)
        json_data[key] = translated_value

        # Menampilkan loading persentase
        percentage = (i + 1) / total_keys * 100
        loading.update_progress(percentage/100)

        time.sleep(0.5)  # Jeda 0.5 detik untuk simulasi

    # Menyimpan hasil terjemahan ke file yang sama
    with open(file_path, 'w') as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)
    loading.stop()
    print()
    print("[*] Translation completed and saved to file.")


if __name__ == "__main__":
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(
        description="Translate JSON file using Google Translate", usage="jsontrans [file_path] [json_lang_dest]")

    # Add arguments to the parser
    parser.add_argument("file_path", nargs="?", help="Path to the JSON file")
    parser.add_argument("json_lang_dest", nargs="?",
                        help="Language ID to which the JSON should be translated")

    # Parse the arguments
    args = parser.parse_args()

    # If no arguments provided, display help and exit
    if not args.file_path or not args.json_lang_dest:
        parser.print_help()
        sys.exit()
    json_lang_dest = args.json_lang_dest
    translate_json_file(args.file_path)
