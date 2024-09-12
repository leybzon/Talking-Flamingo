import os
import re
import sys
from google.cloud import texttospeech
import vertexai
from vertexai.generative_models import GenerativeModel, SafetySetting

# Initialize Vertex AI client
vertexai.init()

# Initialize the Google Cloud Text-to-Speech client
client = texttospeech.TextToSpeechClient()

def generate_speech(ssml, output_filename, gender):
    """
    Generates speech from SSML and saves it to an MP3 file.

    Args:
        ssml (str): The SSML content to be synthesized.
        output_filename (str): The name of the file to save the output MP3.
        gender (str): 'M' for male, 'F' for female voice.
    """
    # Set up the synthesis input from SSML
    synthesis_input = texttospeech.SynthesisInput(ssml=ssml)

    # Select the voice parameters based on the gender
    if gender == 'M':
        ssml_gender = texttospeech.SsmlVoiceGender.MALE
    elif gender == 'F':
        ssml_gender = texttospeech.SsmlVoiceGender.FEMALE
    else:
        raise ValueError("Invalid gender argument. Use 'M' for male or 'F' for female.")

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=ssml_gender
    )

    # Specify the audio configuration
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Save the output to an MP3 file
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Audio content written to "{output_filename}"')

    # Play the generated MP3 file using afplay (Mac-specific)
    os.system(f"afplay {output_filename}")

def generate_ssml(prompt):
    """
    Generates SSML content based on a given prompt using Google Gemini Generative AI.

    Args:
        prompt (str): The prompt to generate SSML content.

    Returns:
        str: Generated SSML content.
    """
    generation_config = {
        "max_output_tokens": 8192,
        "temperature": 1.0,
        "top_p": 0.95,
    }

    safety_settings = [
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH
        )
    ]

    model = GenerativeModel("gemini-experimental")
    
    responses = model.generate_content(
        prompt,
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    ssml = ""
    for response in responses:
        ssml += response.text
    return ssml

def sanitize_ssml(input_text):
    """
    Sanitizes the input SSML text to ensure it starts with <speak> and ends with </speak>.

    Args:
        input_text (str): The SSML text to be sanitized.

    Returns:
        str: Sanitized SSML text.
    """
    # Ensure the text starts with <speak>
    if not input_text.strip().startswith("<speak>"):
        input_text = "<speak>" + input_text

    # Ensure the text ends with </speak>
    if not input_text.strip().endswith("</speak>"):
        input_text = input_text.rstrip() + "</speak>"

    # Remove any invalid XML before <speak> and after </speak>
    sanitized_text = re.sub(r'^.*?<speak>', '<speak>', input_text, flags=re.DOTALL)
    sanitized_text = re.sub(r'</speak>.*$', '</speak>', sanitized_text, flags=re.DOTALL)

    return sanitized_text

def display_usage():
    """
    Displays usage information for the script.
    """
    print("Usage:")
    print("  python flamingo.py <prompt_file> <output_mp3> <gender>")
    print("\nArguments:")
    print("  <prompt_file>   Path to the text file containing the prompt.")
    print("  <output_mp3>    Name of the output MP3 file.")
    print("  <gender>        'M' for male, 'F' for female.")
    print("\nExample:")
    print("  python flamingo.py bob_prompt1.txt bob_output1.mp3 M")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        display_usage()
    else:
        prompt_file = sys.argv[1]
        output_filename = sys.argv[2]
        gender = sys.argv[3].upper()

        # Load the prompt from the file
        with open(prompt_file, "r") as file:
            prompt = file.read()

        # Generate SSML from the prompt
        ssml_text = generate_ssml(prompt)

        # Sanitize the SSML
        ssml_text = sanitize_ssml(ssml_text)
        print(ssml_text)

        # Generate speech from the SSML
        generate_speech(ssml_text, output_filename, gender)

