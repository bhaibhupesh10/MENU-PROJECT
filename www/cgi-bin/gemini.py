#!/usr/bin/python3

import cgi
import cgitb
import os
import google.generativeai as genai

# Enable CGI error reporting
cgitb.enable()

print("Content-Type: text/plain\n")

try:
    # Configure the API key
    genai.configure(api_key="AIzaSyD_NP9TmFcYRtxwkc7SGfQsqHO3S-IX6mc")

    # Define the generation configuration
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    # Create the generative model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    # Start a chat session
    chat_session = model.start_chat(history=[])

    # Parse form data
    form = cgi.FieldStorage()
    prompt = form.getvalue('prompt')

    if not prompt:
        print("No prompt provided.")
        exit()

    # Send the prompt to the model and get the response
    response = chat_session.send_message(prompt)
    print(response.text)

except Exception as e:
    print(f"Error: {str(e)}")

