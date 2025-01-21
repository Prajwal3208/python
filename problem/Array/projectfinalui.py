import os
import cv2
import gradio as gr
import numpy as np
import random
import base64
import time

MAX_SEED = 999999

def tryon(person_img, garment_img, seed, randomize_seed):
    if person_img is None or garment_img is None:
        return None, None, "Empty image"
    if randomize_seed:
        seed = random.randint(0, MAX_SEED)
    
    # Mocked try-on functionality
    # Here we combine the two images side by side as a placeholder
    tryon_result = np.hstack((person_img, garment_img))
    
    return tryon_result, seed, "Success"

example_path = os.path.join(os.path.dirname(__file__), 'assets')

garm_list = os.listdir(os.path.join(example_path, "cloth"))
garm_list_path = [os.path.join(example_path, "cloth", garm) for garm in garm_list]

human_list = os.listdir(os.path.join(example_path, "human"))
human_list_path = [os.path.join(example_path, "human", human) for human in human_list]

css = """
#col-left {
    margin: 0 auto;
    max-width: 430px;
}
#col-mid {
    margin: 0 auto;
    max-width: 430px;
}
#col-right {
    margin: 0 auto;
    max-width: 430px;
}
#col-showcase {
    margin: 0 auto;
    max-width: 1100px;
}
#button {
    color: blue;
}
"""

with gr.Blocks(css=css) as Tryon:
    with gr.Row():
        with gr.Column(elem_id="col-left"):
            imgs = gr.Image(label="Person image", sources='upload', type="numpy")
            example = gr.Examples(
                inputs=imgs,
                examples_per_page=12,
                examples=human_list_path
            )
        with gr.Column(elem_id="col-mid"):
            garm_img = gr.Image(label="Garment image", sources='upload', type="numpy")
            example = gr.Examples(
                inputs=garm_img,
                examples_per_page=12,
                examples=garm_list_path
            )
        with gr.Column(elem_id="col-right"):
            image_out = gr.Image(label="Result", show_share_button=False)
            with gr.Row():
                seed = gr.Slider(
                    label="Seed",
                    minimum=0,
                    maximum=MAX_SEED,
                    step=1,
                    value=0,
                )
                randomize_seed = gr.Checkbox(label="Random seed", value=True)
            with gr.Row():
                seed_used = gr.Number(label="Seed used")
                result_info = gr.Text(label="Response")
            test_button = gr.Button(value="Run", elem_id="button")

    test_button.click(fn=tryon, inputs=[imgs, garm_img, seed, randomize_seed],
                      outputs=[image_out, seed_used, result_info], api_name=False, concurrency_limit=10)

Tryon.queue(api_open=False).launch(show_api=False)
