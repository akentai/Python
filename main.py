import speech_recognition as sr
from google_trans_new import google_translator
import gtts
import playsound
from pynput.keyboard import Key, Listener

LANG_SRC = 'el-GR'
LANG_TGT = 'en'
r = sr.Recognizer()
translator = google_translator()
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


def start_listening(key):
    if key == Key.space:
        return False


def record_audio():
    with sr.Microphone(device_index=2) as source:
        print("Say Something")
        r.adjust_for_ambient_noise(source)
        with Listener(on_press=start_listening) as listener:
            listener.join()
        print("Ready")
        audio = r.listen(source)
        print("Received")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language=LANG_SRC)
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError:
            print("My speech service is down")

        return voice_data


def translate_text(text_in):
    return translator.translate(text_in, lang_src=LANG_SRC, lang_tgt=LANG_TGT)


while True:
    text = record_audio()
    if text == '':
        continue
    elif text == 'exit' or text == 'έξοδος':
        print("App exits")
        break
    print(text)
    translated_text = translate_text(text)
    print(translated_text)
    tts = gtts.gTTS(translated_text, lang=LANG_TGT)
    tts.save('test.mp3')
    playsound.playsound('test.mp3')



