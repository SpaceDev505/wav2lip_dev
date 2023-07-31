
from fastapi import FastAPI
import gradio as gr
import os
import uvicorn
#from generate_audio import generate_audio
# from inference_audio_image import inference2
from inference1 import inference_main
from aws_tts import text_to_speech
import cv2
app = FastAPI()
@app.get('/test')
def test():
    return ('testapp, hello, how are you?')


def convert(segment_length, video, audio):
    return audio

def get_result(input_video, in_image):
    # if input_image == None:
    #     print('12')
    #     result = inference_main(input_video)
    # if input_video == None:
    #     print(input_image)
    #     print('111111111111111111')
    #     result = inference_main(input_image)
    #     # result = "123"
    # cv2.imwrite('123.jpg', in_image)
    if input_video:
        result = inference_main(input_video)
    elif input_video == None:
        # print(in_image)
        img = cv2.cvtColor(in_image, cv2.COLOR_BGR2RGB)
        cv2.imwrite('input.jpg', img)
        img_path = 'input.jpg'
        result = inference_main(img_path)
    return result

block = gr.Blocks().queue()
with block:
    with gr.Row():
        gr.Markdown("## Lip Sync")
    with gr.Row():
        with gr.Column():
            inputs_video = gr.Video(label="Original Video", show_label=True)
            # inputs_image = gr.Image(label='Original Image', show_label=True)
            in_images = gr.Image(source='upload')
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
    runBtn.click(fn=get_result, inputs=[inputs_video, in_images], outputs=[result])

gr.mount_gradio_app(app, block, path='/')
if __name__ =="__main__":
    uvicorn.run(app, port =8000 )