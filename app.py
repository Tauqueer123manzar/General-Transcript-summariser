from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

# Get YouTube video transcript
video_id = 'https://youtu.be/gsIdFo6Tlro'
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Initialize text generation pipeline
text_generation_pipeline = pipeline('text-generation')

# Process transcript with the pipeline
generated_text = text_generation_pipeline(transcript)

# Print or save the generated text
print(generated_text)
