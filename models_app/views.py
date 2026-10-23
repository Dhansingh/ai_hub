from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import openai, requests
from openai import OpenAI
import os
api_key=os.getenv("OPENAI_API_KEY")
@login_required
def dashboard(request):
    models = ['gpt', 'llama', 'gemini', 'perplexity', 'claude']  # Python list
    return render(request, "models_app/dashboard.html", {"models": models})

@login_required
def ai_model_view(request, model_name):
    response_text = ''
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        if model_name == 'gpt':
            openai.api_key = settings.OPENAI_API_KEY
            resp = client.responses.create(
                model="gpt-4o-mini",
                input="write a haiku about ai",
                store=True,
                )   
            response_text = resp.choices[0].message['content']

        elif model_name == 'llama':
            headers = {"Authorization": f"Bearer {settings.LLAMA_API_KEY}"}
            data = {"inputs": prompt}
            resp = requests.post(
                "https://api-inference.huggingface.co/models/meta-llama/LLaMA-2-7b",
                headers=headers, json=data
            )
            response_text = resp.json()[0]['generated_text']

        elif model_name == 'gemini':
            response_text = f"Gemini response placeholder: {prompt}"

        elif model_name == 'perplexity':
            response_text = f"Perplexity response placeholder: {prompt}"

        elif model_name == 'claude':
            response_text = f"Claude response placeholder: {prompt}"

    return render(request, 'models_app/ai_model.html', {'response': response_text, 'model_name': model_name})
