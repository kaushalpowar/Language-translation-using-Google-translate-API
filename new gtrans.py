from googletrans import Translator

source_text = """Yeh ek language translator project hai"""
translator = Translator()

out = translator.translate(source_text ,dest='en')

print(out.text)

