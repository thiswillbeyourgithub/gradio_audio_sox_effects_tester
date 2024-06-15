import soundfile as sf
from pydub import AudioSegment
import torchaudio
import gradio as gr
from typeguard import typechecked


class gradio_audio_sox_effects_tester:
    VERSION: str = "0.0.1"

    @typechecked
    def __init__(
        self,
        path: str,
        ) -> None:
        """
        Initialize the audio cleaning application.

        Parameters:
        path (str): The file path to the audio file to be cleaned.

        This method sets up a Gradio interface with a textbox for specifying SoX effects,
        an audio player for the original audio, an audio player for the cleaned audio,
        and a button to trigger the cleaning process. The cleaning process involves
        applying the specified SoX effects to the audio and converting the cleaned audio
        to MP3 format.
        """


        with gr.Blocks() as app:
            text = gr.Textbox(
                value="""
[
["norm"],  # normalize audio

# isolate voice frequency
# ["highpass", "-1", "100"],
# ["lowpass", "-1", "3000"],
# -2 is for a steeper filtering: removes high frequency and very low ones
    ["highpass", "-2", "50"],
    ["lowpass", "-2", "5000"],

# ["norm"],  # normalize audio

# max silence should be 2s
    ["silence", "-l", "1", "0", "1%", "-1", "2.0", "1%"],

# ["norm"],
]
""",
                lines=10,
            )
            audio_untouched = gr.Audio(
                value=path,
                interactive=True,
                autoplay=False,
            )

            audio_cleaned = gr.Audio(
                value=None,
                interactive=True,
                autoplay=False,
            )

            clean = gr.Button(value="Clean audio")

            @typechecked
            def clean_audio(textbox: str) -> str:
                sox = eval(textbox)
                assert isinstance(sox, list)

                waveform, sample_rate = torchaudio.load(path)
                waveform, sample_rate = torchaudio.sox_effects.apply_effects_tensor(
                        waveform,
                        sample_rate,
                        sox,
                        )

                # write to wav, then convert to mp3
                sf.write("test.wav", waveform.numpy().T, sample_rate, format='wav')
                temp = AudioSegment.from_wav("test.wav")
                temp.export("test.mp3", format="mp3")
                return "test.mp3"

            clean.click(
                fn=clean_audio,
                inputs=[text],
                outputs=[audio_cleaned],
            )

        app.launch(
            inbrowser=True,
        )

if __name__ == "__main__":
    import fire
    fire.Fire(gradio_audio_sox_effects_tester)
