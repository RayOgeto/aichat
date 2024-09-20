from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import openai

# Use the new OpenAI API structure
openai.api_key = settings.OPENAI_API_KEY

@api_view(['POST'])
def chat(request):
    user_message = request.data.get('message', '')

    if not user_message:
        return Response({'error': 'No message provided'}, status=400)

    # OpenAI Chat API call
    try:
        print(f'User message: {user_message}')
        
        response = openai.chat.completions.create(  # This is the new method
            model='whisper-1',  # Use the correct model
            messages=[{"role": "user", "content": user_message}]
        )
        
        print(f"OpenAI response: {response}")

        ai_response = response.choices[0].message['content']

        return Response({'response': ai_response})

    except openai.OpenAIError as e:
        # Log the error message
        print(f"OpenAI error: {e}")
        return Response({'error': str(e)}, status=500)

    except Exception as e:
        # General error logging
        print(f"General error: {e}")
        return Response({'error': 'Internal server error'}, status=500)