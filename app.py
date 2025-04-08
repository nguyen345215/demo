from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your OpenRouter API key
OPENROUTER_API_KEY = "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"

def chat_with_openrouter(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",  # Có thể dùng "openai/gpt-4", "mistralai/mistral-7b-instruct", v.v.
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Lỗi khi gọi OpenRouter: {response.status_code} - {response.text}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_response():
    user_msg = request.args.get("msg")
    gpt_response = chat_with_openrouter(user_msg)
    return gpt_response

if __name__ == "__main__":
    app.run(debug=True)
