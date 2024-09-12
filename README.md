# Talking Flamingo
 Wonderland Cricket at Burning Man recreates the Alice in Wonderland cricket game, where flamingos serve as mallets. Participants use life-sized, lit-up flamingo sculptures with sound effects to play a quirky cricket game with hedgehog "balls." This repo contains scripts to generate SSML scripts and mp3 audio for flamingo voices, adding sound and humor.

This repository contains the source code and prompts for the **Flamingo Croquet Project** created for Burning Man 2004. The project gives voice to the flamingos used in the Wonderland-inspired croquet game, allowing them to express their frustrations, exhaustion, and quirky personalities through generated audio files.

## Repository Contents

- **bob-audio/**: Directory containing generated audio files for Bob, the gruff and angry flamingo.
- **bob_prompt.txt**: Text file containing a prompt for Bob's speech.
- **bob_prompt1.txt**: Alternative prompt file for Bob's speech.
- **marta-audio/**: Directory containing generated audio files for Marta, the weary and overworked flamingo.
- **marta_prompt.txt**: Text file containing a prompt for Marta's speech.
- **marta_prompt1.txt**: Alternative prompt file for Marta's speech.
- **flamingo.py**: Python script that generates SSML from prompts and uses Google Cloud's Text-to-Speech API to create audio files.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/flamingo-croquet-project.git
   cd flamingo-croquet-project
