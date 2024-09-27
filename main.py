from flask import Flask, render_template, request

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
  
@app.route('/generate', methods=['GET', 'POST'])


def generate():
  if request.method == 'POST':  
    prompt = PromptTemplate.from_template("Generate a blog on title {title}?")
    llm = OpenAI(openai_api_key="Secrete key ", temperature=0.3)     #add the serect key here

 
    chain = LLMChain(llm=llm, prompt=prompt)
    prompt = request.json.get('prompt')
    output = chain.run(prompt)
    return output


app.run(host='0.0.0.0',port=5500)

