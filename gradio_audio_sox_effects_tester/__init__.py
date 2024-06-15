import fire

from .gradio_audio_sox_effects_tester import gradio_audio_sox_effects_tester

def cli_launcher() -> None:
    fire.Fire(gradio_audio_sox_effects_tester)

if __name__ == "__main__":
    cli_launcher()