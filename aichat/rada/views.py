from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import openai

#------------------------------------------
MALARIA_SYMPTOMS =[
    'fever', 'chills' , 'sweating' , 'headache' ,
    'nausea' , 'vomiting' , 'diarrhea', 'fatigue'
]

def diagnose_malaria(symptoms):
    user_symptoms = symptoms.lower().replace(",", "").split()  # Normalize input symptoms to lowercase and split into a list
    matched_symptoms = [symptom for symptom in user_symptoms if symptom in MALARIA_SYMPTOMS]  # Match symptoms

    symptom_count = len(matched_symptoms)  # Count matched symptoms

    if symptom_count >= 2:
        return 'wa wa wa wa, kumbavu zangu. You may have malaria; please consult your doctor.'
    else:
        return 'Congratulations, no malaria detected, but it is still advisable to consult a doctor.'
   
@api_view(['POST'])
def diagnose(request):
    symptoms = request.data.get('symptoms')
    if not symptoms:
        return Response({"diagnosis": "provide symptoms"}, status=400)
    
    diagnosis = diagnose_malaria(symptoms)
    return Response({"diagnosis": diagnosis})
#------------------------------------------

# # Use the new OpenAI API structure
# openai.api_key = settings.OPENAI_API_KEY

# @api_view(['POST'])
# def chat(request):
#     user_message = request.data.get('message', '')

#     if not user_message:
#         return Response({'error': 'No message provided'}, status=400)

#     # OpenAI Chat API call
#     try:
#         print(f'User message: {user_message}')
        
#         response = openai.chat.completions.create(  # This is the new method
#             model='whisper-1',  # Use the correct model
#             messages=[{"role": "user", "content": user_message}]
#         )
        
#         print(f"OpenAI response: {response}")

#         ai_response = response.choices[0].message['content']

#         return Response({'response': ai_response})

#     except openai.OpenAIError as e:
#         # Log the error message
#         print(f"OpenAI error: {e}")
#         return Response({'error': str(e)}, status=500)

#     except Exception as e:
#         # General error logging
#         print(f"General error: {e}")
#         return Response({'error': 'Internal server error'}, status=500)