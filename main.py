import numpy as np
import soundfile as sf
from kokoro import KPipeline


def main():
    print("Hello from tts-kokoro!")

    pipeline = KPipeline(lang_code="a")

    with open("en.txt", "r") as r:
        text_list = [line.strip() for line in r]

    text = " ".join(text_list)
    print(text)
    print()

    generator = pipeline(text, voice="af_heart")
    audio_chunks = []
    for i, (gs, ps, audio) in enumerate(generator):
        print(i, gs, ps)
        audio_chunks.append(audio)

    full_audio = np.concatenate(audio_chunks)
    sf.write("output.wav", full_audio, 24000)


if __name__ == "__main__":
    main()
