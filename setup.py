
from setuptools import setup, find_packages
from setuptools.command.install import install

setup(
    name="gradio_audio_sox_effects_tester",
    version="0.0.1",
    description="gradio gui to compare sox commands for audio editing",
    long_description="gradio gui to compare sox commands for audio editing",
    url="https://github.com/thiswillbeyourgithub/gradio_audio_sox_effects_tester",
    packages=find_packages(),

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    license="GPLv3",
    keywords=[],
    python_requires=">=3.11",

    entry_points={
        'console_scripts': [
            'gradio_audio_sox_effects_tester=gradio_audio_sox_effects_tester.__init__:cli_launcher',
        ],
    },

    install_requires=[
        "fire >= 0.6.0",
        "typeguard >= 4.3.0",

        "pydub >= 0.25.1",
        "soundfile  >= 0.12.1",
        "torchaudio >= 2.3.1",
        "gradio >= 4.36.1",
    ],
)
