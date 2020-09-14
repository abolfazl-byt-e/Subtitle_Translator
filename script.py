from googletrans import Translator
import webvtt

translator = Translator()
# result = translator.translate("hello ,nodjs how are you.", dest="fa").text
# result = result.encode('utf-8').decode('utf-8')
# print(result)

with open("./vtt/translated.vtt", "a+") as f:
    f.write("WEBVTT\n\n")

    captions = webvtt.read("./vtt/original.vtt")
    for caption in captions:
        # print(caption.start,"-->", caption.end)
        f.write(caption.start)
        f.write(" --> ")
        f.write(caption.end)
        f.write("\n")
        # print(translator.translate(caption.text, src="en", dest="fa").text)
        f.write(translator.translate(caption.text, src="en", dest="fa").text)
        f.write("\n\n")
        # print()
