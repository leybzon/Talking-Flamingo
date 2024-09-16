# Talking Flamingo

Wonderland Cricket at Burning Man recreates the iconic **Alice in Wonderland** cricket game, where flamingos serve as mallets. Participants use life-sized, lit-up flamingo sculptures with sound effects to play a quirky cricket game with hedgehog "balls." This repository contains scripts to generate SSML scripts and MP3 audio for flamingo voices, adding sound and humor to the game.

This repository holds the source code and prompts for the **Flamingo Croquet Project** created for Burning Man 2004. The project gives voice to the flamingos used in the Wonderland-inspired croquet game, allowing them to express their frustrations, exhaustion, and quirky personalities through generated audio files.

This project uses the Google Gemini AI Model to generate SSML scripts and the Google Text-to-Speech engine to synthesize speech from those scripts.

## Repository Contents

- **bob-audio/**: Directory containing generated audio files for Bob, the gruff and angry flamingo.
- **bob_prompt.txt**: Text file containing a prompt for Flamingo Bob's speech.
- **bob_prompt1.txt**: Alternative prompt file for Bob's speech.
- **marta-audio/**: Directory containing generated audio files for Marta, the weary and overworked flamingo.
- **marta_prompt.txt**: Text file containing a prompt for Marta's speech.
- **marta_prompt1.txt**: Alternative prompt file for Marta's speech.
- **flamingo.py**: Python script that generates SSML from prompts and uses Google Cloud's Text-to-Speech API to create audio files.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/leybzon/flamingo-croquet-project.git
cd flamingo-croquet-project
```

### 2. Install Required Dependencies
Ensure you have Python 3 installed. Install the required Python packages:
```bash
pip install google-cloud-texttospeech vertexai
```

### 3. Set Up Google Cloud Credentials
Ensure you have set up your Google Cloud credentials to use the Text-to-Speech API. You can follow the [Google Cloud documentation](https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries) for instructions.

Export the credentials:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
```

## Usage

The `flamingo.py` script is used to generate audio files from prompts. You can specify a prompt file, output MP3 filename, and the desired voice gender (`M` for male, `F` for female) as arguments.

### Example
```bash
python3 flamingo.py marta_prompt.txt marta-audio/00006.mp3 F
```

This command will:
1. Read the prompt from `marta_prompt.txt`.
2. Generate SSML based on the prompt.
3. Synthesize speech using Google Cloud's Text-to-Speech API.
4. Save the output as an MP3 file in the `marta-audio/` directory with the filename `00006.mp3`.

### Script Arguments
```bash
python3 flamingo.py <prompt_file> <output_mp3> <gender>
```

- **`<prompt_file>`**: Path to the text file containing the prompt (e.g., `marta_prompt.txt`).
- **`<output_mp3>`**: Path where the generated MP3 file will be saved (e.g., `marta-audio/00006.mp3`).
- **`<gender>`**: The gender of the voice to be used. Use `M` for male and `F` for female.

If no arguments are provided, the script will display usage instructions.


