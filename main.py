
from fastapi import FastAPI
import gradio as gr
import os
import uvicorn
#from generate_audio import generate_audio
# from inference_audio_image import inference2
from inference import inference_main
from aws_tts import text_to_speech
app = FastAPI()
@app.get('/test')
def test():
    return ('testapp, hello, how are you?')


def convert(segment_length, video, audio):
    return audio

def get_result(input_video, input_image):
    # if input_video == None:
    #     result = inference2(input_image)
    if input_image == None:
        print('12')
        # result = inference_main(input_video)
    return result

block = gr.Blocks().queue()
with block:
    with gr.Row():
        gr.Markdown("## Lip Sync")
    with gr.Row():
        with gr.Column():
            inputs_video = gr.Video(label="Original Video", show_label=True)
            inputs_image = gr.Image(source='upload')
            input_text = gr.Textbox(label="Please input text you want")
            select_lang = gr.Dropdown(['Chinese(Mandarin)', 'Chinese(Cantonese)', 'English(US)', 'English(UK)', 'Spanish(Spain)', 'French(France)'])
            audio = gr.outputs.Audio(type="numpy", label=None)
            with gr.Row():
                audioBtn = gr.Button("Generate Audio")
                runBtn = gr.Button("Generate Video")
        with gr.Column():
            # gallery = gr.Gallery(label="Generated images", show_label=False)
            result = gr.Video(label="Generated Video", show_label=True)
    audioBtn.click(fn=text_to_speech, inputs=[input_text, select_lang], outputs=[audio])
    runBtn.click(fn=get_result, inputs=[inputs_video, inputs_image], outputs=[result])

gr.mount_gradio_app(app, block, path='/')
if __name__ =="__main__":
    uvicorn.run(app, port =8000 )

