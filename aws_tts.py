
import boto3
import wave

# Replace 'YOUR_ACCESS_KEY' and 'YOUR_SECRET_KEY' with your actual AWS credentials.
access_key = 'AKIAXJMRFKAOM24BF3GN'
secret_key = 'LYTzUKFTgU/fKeAoX0qeVHkjMk2sWnTNIINefvSz'
region_name = 'us-west-2'  # Change this to your desired AWS region

# Initialize the Amazon Polly client
polly_client = boto3.client('polly', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region_name)

def text_to_speech(text, lang):
    voice_id = 'Joanna'
    output_format = 'pcm'  # Change the output format to 'pcm' for raw PCM data
    output_file = '1.wav'  # Change the output file name to 'output.wav'
    if lang  == "Chinese(Mandarin)":
        lang_code = "cmn-CN"
        voice_id = 'Zhiyu'
    elif lang  == "Chinese(Cantonese)":
        lang_code = "yue-CN"
        voice_id = 'Zhiyu'
    elif lang  == "English(US)":
        lang_code = "en-US"
        voice_id = 'Joanna'
    elif lang  == "English(UK)":
        lang_code = "en-GB"
        voice_id = 'Amy'
    elif lang  == "Spanish(Spain)":
        lang_code = "es-US"
        voice_id = 'Lucia'
    elif lang  == "French(France)":
        lang_code = "fr-FR"
        voice_id = 'Celine'

    try:
        # Call Amazon Polly to synthesize the speech
        response = polly_client.synthesize_speech(
            Text=text,
            OutputFormat=output_format,
            VoiceId=voice_id,
            LanguageCode = lang_code
        )

        # Save the audio stream as raw PCM data
        with open(output_file, 'wb') as file:
            file.write(response['AudioStream'].read())

        # Convert the raw PCM data to a valid WAV file
        with open(output_file, 'rb') as pcm_file:
            pcm_data = pcm_file.read()

        with wave.open(output_file, 'wb') as wav_file:
            wav_file.setnchannels(1)  # Mono audio
            wav_file.setsampwidth(2)  # 16-bit audio
            wav_file.setframerate(16000)  # Sample rate (adjust as needed)
            wav_file.writeframes(pcm_data)

        print(f'Successfully generated speech. Saved as "{output_file}"')
        return output_file

    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    text_to_speech("He, it is a test")
