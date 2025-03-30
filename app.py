import gradio as gr
import pandas as pd
import os
import warnings
from gtts import gTTS
from deep_translator import GoogleTranslator
from langdetect import detect
dataset =  pd.read_csv(r"C:\Users\thila\Downloads\NARESH IT  PYTHON FSDS NOTES\MY PROJECTS\Language Translation\language.csv")
dataset
dataset.isnull().sum()
dataset.dropna(inplace=True)
dataset
langlist = tuple(dataset['name'].tolist())
langcode = dataset['iso'].tolist()
lang_array = {langlist[i]: langcode[i] for i in range(len(langlist))}
import gradio as gr
import warnings
speech_langs = {"en": "English", "es": "Spanish", "fr": "French", "de": "German", "hi": "Hindi", "zh-CN": "Chinese"}
def translate_and_speak(text, selected_option):
    if len(text) > 0:
        try:
            detected_lang = detect(text)  # Detect input language
            source_lang = "en" if detected_lang == "en" else detected_lang  # Handle Tanglish

            translator = GoogleTranslator(source=source_lang, target=lang_array[selected_option])
            output = translator.translate(text)

            audio_file = None
            if lang_array[selected_option] in speech_langs:
                tts = gTTS(text=output, lang=lang_array[selected_option], slow=False)
                audio_file = "translated_audio.mp3"
                tts.save(audio_file)

            return output, audio_file
        except Exception as e:
            return str(e), None
    return "", None
demo = gr.Interface(
    fn=translate_and_speak,
    inputs=[gr.Textbox(label="Write Your Text"), gr.Dropdown(choices=list(langlist), label="Select Language to Translate")],
    outputs=[gr.Textbox(label="Translated Text"), gr.Audio(label="Translated Audio")],
    title="Language Translation App",
    description="Translate text into different languages."
)

demo.launch()























