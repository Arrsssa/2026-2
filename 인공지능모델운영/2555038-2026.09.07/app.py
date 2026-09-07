import gradio as gr


def greet(name):
    if not name.strip():
        return "Please enter your name."
    return f"Hello, {name}! CI/CD deployment is working."


demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Your name"),
    outputs=gr.Textbox(label="Result"),
    title="CI/CD Demo",
    description="Python + Gradio + Docker + GitHub Actions + Hugging Face Spaces",
)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
