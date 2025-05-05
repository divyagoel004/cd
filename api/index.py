from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load Hugging Face summarization pipeline
# You can swap "t5-small" with any other summarization-compatible model
summarizer = pipeline("summarization", model="t5-small")  # :contentReference[oaicite:1]{index=1}

@app.route("/", methods=["GET", "POST"])
def home():
    summary = None
    if request.method == "POST":
        text = request.form.get("text")
        if text:
            # Generate summary; adjust max_length/min_length as needed
            summary_objs = summarizer(text, max_length=150, min_length=40, do_sample=False)  # :contentReference[oaicite:2]{index=2}
            summary = summary_objs[0]["summary_text"]
    return render_template(r"C:\Users\divya\Downloads\vercel-app\templates\index.html", summary=summary)

if __name__ == "__main__":
    # Local dev run
    app.run(debug=True, port=3000)
