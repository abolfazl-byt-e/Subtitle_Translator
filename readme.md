# subtitile translator (*english to persian*)
A app in python language to translate SRT english subtitles to persian language.
</ br>
*python* and *flask* are used.
## how to run
```
git clone https://github.com/abolfazlbyte/Subtitle_Translator.git
cd Subtitle_Translator
pip install python3-venv
python -m venv .venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
export FLASK_ENV=development
python init.py  #{Only for the first time}
python -m flask run --port=5000  #{or another port}
go to localhost:{port} in browser
```
