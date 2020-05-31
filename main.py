"""Representing an APP"""
from flask import Flask, render_template, request
from vigenere_cipher import VigenereCipher

APP = Flask(__name__)


@APP.route('/', methods=['GET'])
def main():
    """Returns home page"""
    return render_template('index.html')


@APP.route('/result', methods=['POST', 'GET'])
def result_page():
    """Returns result page with encoded or decoded
    message"""
    keyword = request.form['keyword']
    choice = request.form['choice']
    message = request.form['message']
    cipher = VigenereCipher(keyword)
    if choice == 'encode':
        result = cipher.encode(message)
    else:
        result = cipher.decode(message)
    if result is None:
        return render_template('exception.html')
    return render_template('result.html', result=result)


if __name__ == '__main__':
    APP.run(port=8000)
