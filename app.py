import pprint
import google.generativeai as palm
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
load_dotenv()
api_key1=os.getenv("API_KEY")
palm.configure(api_key=api_key1)


#models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
#model = models[0].name

app = Flask(__name__)

@app.route('/')
def chatbot():
    return render_template('index.html')

@app.route('/generate_response', methods=['POST'])
def generate_response():
    data = request.get_json()
    prompt = data.get('user_input', '')
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        max_output_tokens=800,
    )
    response = completion.result
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5000 , host="0.0.0.0")
