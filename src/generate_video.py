import os
import random
from typing import List
from gtts import gTTS
from moviepy import (
    CompositeVideoClip, CompositeAudioClip,
    VideoFileClip, AudioFileClip, ImageClip, TextClip,
    concatenate_videoclips, concatenate_audioclips
)
from rich.console import Console
from rich.progress import track

def generate_speech(text: str, fileName: str):
    myobj = gTTS(text=text, lang='fr', slow=False, tld='fr')
    myobj.save(fileName)
    return

def generate_video(
        content: str,
        video_file: str,
        outfile: str,
        image_file: str = '',
        offset: int = 0,
        duration: int = 0):
    audio_comp, text_comp = generate_audio_text(split_text(content))

    audio_comp_list = []

    for audio_file in track(audio_comp, description='Stitching Audio...'):
        audio_comp_list.append(AudioFileClip(audio_file))
    audio_comp_stitch = concatenate_audioclips(audio_comp_list)
    audio_comp_stitch.write_audiofile('temp_audio.mp3', fps=44100)

    audio_duration = audio_comp_stitch.duration
    if duration == 0:
        duration = audio_duration

    audio_comp_stitch.close()

    vid_clip = VideoFileClip(video_file).subclipped(offset)
    vid_clip = vid_clip.resized((720, 1280))

    original_audio = vid_clip.audio

    audio_clip = AudioFileClip('temp_audio.mp3').subclipped(0, duration)

    remaining_audio_duration = vid_clip.duration - audio_clip.duration

    if remaining_audio_duration > 0:
        original_audio_clip = original_audio.subclipped(-remaining_audio_duration)
        final_audio = concatenate_audioclips([audio_clip, original_audio_clip])
    else:
        final_audio = audio_clip

    vid_clip = vid_clip.with_audio(final_audio)

    vid_clip = CompositeVideoClip([vid_clip, concatenate_videoclips(text_comp).with_position(('center', 360))])

    vid_clip.write_videofile(outfile, audio_codec='aac')
    vid_clip.close()


def split_text(text: str, delimiter: str = ','):
    return text.split(delimiter)

def generate_audio_text(fulltext: List[str]):
    audio_comp = []
    text_comp = []

    for idx, text in track(enumerate(fulltext), description='Synthesizing Audio...'):
        if text.strip() == "":
            continue

        audio_file = f"temp_assets/audio_{idx}.mp3"
        generate_speech(text.strip(), audio_file)

        audio_duration = AudioFileClip(audio_file).duration

        text_clip = TextClip(
            text=text,
            font='./fonts/RobotoMono-BoldItalic.ttf',
            font_size=32,
            color="white",
            text_align='center',
            method='caption',
            size=(660, None)
        )

        text_clip = text_clip.with_duration(audio_duration)

        audio_comp.append(audio_file)
        text_comp.append(text_clip)

    return audio_comp, text_comp

def get_random_video_file():

    video_list = []

    for path, subdirs, files in os.walk('./video'):
        for name in files:
            if name.endswith('.mp4'):
                video_list.append(os.path.join(path, name))


    return str(video_list[random.randrange(len(video_list))])

def start_generate_video(text: str):
    console = Console()

    if not os.path.exists("temp_assets"):
        os.mkdir("temp_assets")

    video_file: str = get_random_video_file()
    console.print("\n\n[light_green] Task Starting\n\n")
    generate_video(content=text,
                   video_file=video_file,
                   image_file='',
                   outfile="./output/video.mp4",
                   offset=0)

    console.print("\n\n[light_green] Completed!")

    return True
