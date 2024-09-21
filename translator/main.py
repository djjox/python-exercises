import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

# Create the main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("500x300")

# Create a function for translating text
def translate_text():
    source_text = text_box.get(1.0, tk.END).strip()
    src_lang = source_lang.get()
    dest_lang = target_lang.get()
    
    # Use deep_translator's GoogleTranslator
    translation = GoogleTranslator(source=src_lang, target=dest_lang).translate(source_text)
    
    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, translation)

# Label and text box for the input text
input_label = tk.Label(root, text="Enter text to translate:", font=("Arial", 12))
input_label.pack(pady=10)

text_box = tk.Text(root, height=5, width=40)
text_box.pack(pady=10)

# Dropdowns for source and target languages
source_lang = tk.StringVar(root)
target_lang = tk.StringVar(root)

source_lang.set("en")  # Default to English
target_lang.set("es")  # Default to Spanish

source_lang_label = tk.Label(root, text="Source Language:", font=("Arial", 10))
source_lang_label.pack()

source_lang_menu = ttk.Combobox(root, textvariable=source_lang, values=['en', 'es', 'fr', 'de', 'it'], width=30)
source_lang_menu.pack(pady=5)

target_lang_label = tk.Label(root, text="Target Language:", font=("Arial", 10))
target_lang_label.pack()

target_lang_menu = ttk.Combobox(root, textvariable=target_lang, values=['en', 'es', 'fr', 'de', 'it'], width=30)
target_lang_menu.pack(pady=5)

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text, font=("Arial", 12))
translate_button.pack(pady=10)

# Text box for displaying the result
result_label = tk.Label(root, text="Translated Text:", font=("Arial", 12))
result_label.pack(pady=10)

result_box = tk.Text(root, height=5, width=40)
result_box.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()