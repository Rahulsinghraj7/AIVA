import ollama

def generate_content(prompt, content_type):

    final_prompt = f"""
    Generate a professional {content_type}
    for the following request:

    {prompt}
    """

    response = ollama.chat(
        model="phi3:mini",
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    )

    return response["message"]["content"]