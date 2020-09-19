from googletrans import Translator
import webvtt

translator = Translator()

#TODO get the file
file_name = input('FILE NAME: enter file name with extention  .vtt .srt .sbv\n')
x = file_name[:-4]
y = file_name[-4:]
file_name_persian = x + "_persian" + y
print(file_name)
print(file_name_persian)

#TODO functions
def vtt_translate(file_name, file_name_persian):
    with open("./pase_it/%s"%file_name_persian, "a+") as f:
        f.write("WEBVTT\n\n")

        captions = webvtt.read("./pase_it/%s"%file_name)
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
        f.close()
        print("Done. --> /pase_it/%s"%file_name_persian)

def srt_translate(file_name, file_name_persian):
    with open("./pase_it/%s"%file_name_persian, "a+") as f:

        counter = 1
        captions = webvtt.from_srt("./pase_it/%s"%file_name)
        for caption in captions:
            f.write(str(counter))
            f.write("\n")
            # print(caption.start,"-->", caption.end)
            f.write(caption.start)
            f.write(" --> ")
            f.write(caption.end)
            f.write("\n")
            # print(translator.translate(caption.text, src="en", dest="fa").text)
            f.write(translator.translate(caption.text, src="en", dest="fa").text)
            f.write("\n\n")
            # print()
            counter +=1
        f.close()
        print("Done. --> /pase_it/%s"%file_name_persian)

#TODO detect file format
if y == ".srt":
    srt_translate(file_name, file_name_persian)
elif y == ".vtt":
    vtt_translate(file_name, file_name_persian)
elif y == ".sbv":
    pass
else:
    print("dont detect!!!")