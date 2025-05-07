from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="t5-small")

@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']

    # Perform summarization
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    summarized_text = summary[0]['summary_text']

    return jsonify({'summary': summarized_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

