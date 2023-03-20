import gradio as gr
import pandas as pd
import numpy as np

np.set_printoptions(suppress=True)

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=2):
            file_name = gr.Textbox(label="File name", placeholder="Put file name here", show_label=False)
            lines_number = gr.Number(label="Put number of lines to display", precision=0)
            decision_class = gr.Checkbox(label="Display quantity of decision classes")
            class_size = gr.Checkbox(label="Display size of each decision class")
            with gr.Row():
                submit = gr.Button("Submit")
                clear = gr.Button("Clear")

        with gr.Column(scale=5):
            board = gr.DataFrame(interactive=False)
            textbox = gr.Textbox(interactive=False)


    def open_text(file, rows, check1, check2):
        file_path = "dane/" + file + ".txt"
        try:
            df = pd.read_csv(file_path, sep=' ', header=None)
        except FileNotFoundError:
            raise gr.Error("File not found")

        ob_size = len(df.index)
        atrib_size = len(df.columns)

        options_path = "dane/" + file + "-type.txt"
        decisionType = []
        with open(options_path) as file:
            for line in file:
                decisionType.append(line[-2])

        s_count = 0
        n_count = 0
        for i in decisionType:
            if i == 's':
                s_count += 1
            if i == 'n':
                n_count += 1

        result = f'Objects: {ob_size}\nAttributes: {atrib_size}\n'

        if check1:
            result = result + f'List of attribute types (s - symbolic, n - numeric): {decisionType}\n'
        if check2:
            result = result + f'Size of numeric class: {n_count}\n' + f"Fize of symbolic class: {s_count}"
        return [df.iloc[0:rows], result]


    submit.click(open_text, inputs=[file_name, lines_number, decision_class, class_size], outputs=[board, textbox])

demo.launch()
