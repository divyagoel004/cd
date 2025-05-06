from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)


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

if __name__ == "__main__":
    # Local dev run
    port = int(os.environ.get("PORT", 5000))  # Use Render-provided PORT
    app.run(host="0.0.0.0", port=port, debug=True)
