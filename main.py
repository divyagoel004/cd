from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="t5-small")

@app.route("/", methods=["GET", "POST"])
def home():
    summary = None
    if request.method == "POST":
        text = request.form.get("text")
        if text:
            summary_objs = summarizer(text, max_length=150, min_length=40, do_sample=False)
            summary = summary_objs[0]["summary_text"]
    return render_template("index.html", summary=summary)

@app.route("/api/summarize", methods=["GET" , "POST"])
def api_summarize():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']
    summary_objs = summarizer(text, max_length=150, min_length=40, do_sample=False)
    summarized_text = summary_objs[0]['summary_text']
    return jsonify({'summary': summarized_text})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)

