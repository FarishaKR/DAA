from flask import Flask, render_template, request
import os
import time

from utils.file_reader import read_file
from utils.preprocess import preprocess
from utils.similarity import calculate_similarity

from algorithms.naive import naive_search
from algorithms.kmp import kmp_search
from algorithms.rabin_karp import rabin_karp
from algorithms.boyer_moore import boyer_moore

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():

    file = request.files['file']
    pattern = request.form['pattern']
    algorithm = request.form['algorithm']

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    text = read_file(filepath)
    text = preprocess(text)
    pattern = preprocess(pattern)

    start = time.time()

    if algorithm == 'Naive':
        positions = naive_search(text, pattern)

    elif algorithm == 'KMP':
        positions = kmp_search(text, pattern)

    elif algorithm == 'Rabin-Karp':
        positions = rabin_karp(text, pattern)

    elif algorithm == 'Boyer-Moore':
        positions = boyer_moore(text, pattern)

    end = time.time()

    execution_time = round(end - start, 6)

    total_matches = len(positions)

    similarity = calculate_similarity(text, pattern)

    highlighted_text = text.replace(
        pattern,
        f'<mark>{pattern}</mark>'
    )

    return render_template(
        'result.html',
        positions=positions,
        total_matches=total_matches,
        execution_time=execution_time,
        algorithm=algorithm,
        similarity=similarity,
        highlighted_text=highlighted_text
    )


if __name__ == '__main__':
    app.run(debug=True)