from tkinter import *
from tkinter import ttk
import requests


# Function to perform translation using Google Translate API
def translate_text():
    try:
        input_text = text_entry.get(1.0, END).strip()
        if not input_text:
            return

        # Get selected destination language
        dest_lang = language_codes[destination_language.get()]

        # Google Translate API endpoint
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={dest_lang}&dt=t&q={input_text}"

        # Send GET request to the API
        response = requests.get(url)
        response.raise_for_status()

        # Parse and display translated text
        translated_text = response.json()[0][0][0]
        translated_entry.delete(1.0, END)
        translated_entry.insert(END, translated_text)

    except Exception as e:
        print(f"Translation error: {e}")


# Create the main window
root = Tk()
root.geometry('600x400')
root.title('Language Translator')

# Label for source language
source_label = Label(root, text="Enter text to translate:")
source_label.pack()

# Text entry for input text
text_entry = Text(root, height=5, wrap=WORD)
text_entry.pack()

# Label for destination language selection
destination_label = Label(root, text="Select destination language:")
destination_label.pack()

# Get the list of languages using ISO-639 standard
# You can find ISO-639 language codes and names from:
# https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
language_codes = {
    'Afrikaans': 'af',
    'Albanian': 'sq',
    'Amharic': 'am',
    'Arabic': 'ar',
    'Armenian': 'hy',
    'Azerbaijani': 'az',
    'Basque': 'eu',
    'Belarusian': 'be',
    'Bengali': 'bn',
    'Bosnian': 'bs',
    'Bulgarian': 'bg',
    'Catalan': 'ca',
    'Cebuano': 'ceb',
    'Chichewa': 'ny',
    'Chinese (Simplified)': 'zh-CN',
    'Chinese (Traditional)': 'zh-TW',
    'Corsican': 'co',
    'Croatian': 'hr',
    'Czech': 'cs',
    'Danish': 'da',
    'Dutch': 'nl',
    'English': 'en',
    'Esperanto': 'eo',
    'Estonian': 'et',
    'Filipino': 'tl',
    'Finnish': 'fi',
    'French': 'fr',
    'Frisian': 'fy',
    'Galician': 'gl',
    'Georgian': 'ka',
    'German': 'de',
    'Greek': 'el',
    'Gujarati': 'gu',
    'Haitian Creole': 'ht',
    'Hausa': 'ha',
    'Hawaiian': 'haw',
    'Hebrew': 'iw',
    'Hindi': 'hi',
    'Hmong': 'hmn',
    'Hungarian': 'hu',
    'Icelandic': 'is',
    'Igbo': 'ig',
    'Indonesian': 'id',
    'Irish': 'ga',
    'Italian': 'it',
    'Japanese': 'ja',
    'Javanese': 'jw',
    'Kannada': 'kn',
    'Kazakh': 'kk',
    'Khmer': 'km',
    'Korean': 'ko',
    'Kurdish (Kurmanji)': 'ku',
    'Kyrgyz': 'ky',
    'Lao': 'lo',
    'Latin': 'la',
    'Latvian': 'lv',
    'Lithuanian': 'lt',
    'Luxembourgish': 'lb',
    'Macedonian': 'mk',
    'Malagasy': 'mg',
    'Malay': 'ms',
    'Malayalam': 'ml',
    'Maltese': 'mt',
    'Maori': 'mi',
    'Marathi': 'mr',
    'Mongolian': 'mn',
    'Myanmar (Burmese)': 'my',
    'Nepali': 'ne',
    'Norwegian': 'no',
    'Pashto': 'ps',
    'Persian': 'fa',
    'Polish': 'pl',
    'Portuguese': 'pt',
    'Punjabi': 'ma',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Samoan': 'sm',
    'Scots Gaelic': 'gd',
    'Serbian': 'sr',
    'Sesotho': 'st',
    'Shona': 'sn',
    'Sindhi': 'sd',
    'Sinhala': 'si',
    'Slovak': 'sk',
    'Slovenian': 'sl',
    'Somali': 'so',
    'Spanish': 'es',
    'Sundanese': 'su',
    'Swahili': 'sw',
    'Swedish': 'sv',
    'Tajik': 'tg',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Thai': 'th',
    'Turkish': 'tr',
    'Ukrainian': 'uk',
    'Urdu': 'ur',
    'Uzbek': 'uz',
    'Vietnamese': 'vi',
    'Welsh': 'cy',
    'Xhosa': 'xh',
    'Yiddish': 'yi',
    'Yoruba': 'yo',
    'Zulu': 'zu'
}

# Combobox for selecting destination language
destination_language = ttk.Combobox(root, values=list(language_codes.keys()), width=50)
destination_language.pack()
destination_language.set('English')  # Default selection

# Button to trigger translation
translate_button = Button(root, text='Translate', command=translate_text)
translate_button.pack()

# Label for translated output
translated_label = Label(root, text="Translated text:")
translated_label.pack()

# Text entry for translated text display
translated_entry = Text(root, height=5, wrap=WORD)
translated_entry.pack()

# Start the tkinter event loop
root.mainloop()
