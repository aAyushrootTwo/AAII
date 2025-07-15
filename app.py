from flask import Flask, render_template, request
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyBkUxc1zRgvumzIRaqOyR9vTYt2mEnOxDI")

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.form['topic']
    prompt = f"Write a detailed, SEO-friendly blog post on the topic: {topic}"
    
    try:
        response = model.generate_content(prompt)
        blog = response.text
    except Exception as e:
        blog = f"Error generating blog: {str(e)}"
    
    return render_template('index.html', blog=blog)

if __name__ == '__main__':
    app.run(debug=True)
