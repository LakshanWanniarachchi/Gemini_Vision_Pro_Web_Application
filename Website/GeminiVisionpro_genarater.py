import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
from PIL import Image



genai.configure(api_key="AIzaSyDu5pwtfW3SaalRL9ZdYKPHKA7OR00movw")



def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)
    



def genarate_text(img_dir, message):
    
    img = Image.open(img_dir)
    # img.show()

   
    model = genai.GenerativeModel('gemini-pro-vision')

    response = model.generate_content(img)

    to_markdown(response.text)

    # print(response.candidates)

    response = model.generate_content([message, img], stream=True)
    response.resolve()
    
    return response.text