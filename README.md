## LIM

This is amsimple Streamlit web application that integrates with Google's Gemini API.The Image.py describes about the image uploaded

## Features
- Uses Google's Gemini-1.5 Flash model for text generation
- Interactive web-based interface powered by Streamlit
- Simple and easy-to-use chatbot

## Creating the envinorment and Activating the envinorment
```bash
conda create -p venv python==3.10 -y
```

Ensure you install
Python-3.10+
Pip

```bash
conda activate venv/
```


### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up API Key
Create a `.env` file in the root directory and add your Google API key:
```env
Google_api_key=your_google_api_key_here
```

## Usage
Run the Streamlit application:
```bash
streamlit run Image info.py
```

Upload the image and Enter a query in the input field and click "Submit" to get info of the image.This is for the Image info.py


## .gitignore
upload all the files which you don't want to share to others or push to github
like 
venv/(which are very large)
.env(To protect yoyr API keys)

## File Structure
```
|-- your-repo-name/
    |-- app.py
    |-- Image info.py
    |-- requirements.txt
    |-- .env
    |-- .gitignore
    |-- README.md
```

## License
This project is licensed under the MIT License.



