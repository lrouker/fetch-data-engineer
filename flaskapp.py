from flask import Flask, request
from text_similarity import RatingGenerator
import text_parser
app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_texts():
    text1=request.form['text1']
    text2=request.form['text2']

    list1 = text_parser.text_to_list(text1)
    list2 = text_parser.text_to_list(text2)

    rg = RatingGenerator()

    return str(rg.rate(list1, list2))