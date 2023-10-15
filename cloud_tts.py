from google.cloud import texttospeech
import os

# Initialize the client

def google_text_to_speech(text):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "tts.json"
    client = texttospeech.TextToSpeechClient()

    # Text to be converted to speech
    # input_text = "Hello, How are you?"
    input_text = text
    # Configure the voice settings
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Wavenet-F",  # You can choose a different voice name from the available options
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,  # Choose desired audio encoding
        speaking_rate=1.0,  # Adjust speaking rate as needed
    )

    # Generate the synthesis request
    synthesis_input = texttospeech.SynthesisInput(text=input_text)
    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    # Save the audio content to a file
    output_audio_path = "output.mp3"
    with open(output_audio_path, "wb") as audio_file:
        audio_file.write(response.audio_content)

    print("Audio content written to file:", output_audio_path)
    return output_audio_path
if __name__ == '__main__':
    google_text_to_speech("what is that")    

