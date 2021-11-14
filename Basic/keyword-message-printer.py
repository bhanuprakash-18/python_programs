import pyperclip, sys

detail_info = {
    "bhanu":"He is born on feb 18, 2001.",
    "vishnu": "He is born on dec 28, 2001",
    "srikanth": "He is born on july 21, 2001",
    "chanakya": "He is born on march 26, 2001"
}

if len(sys.argv) < 2:
    print('Usage: py filename.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in detail_info:
    pyperclip.copy(detail_info[keyphrase])
    print("Copied to clip board succesfully")
else:
    print("There is no keyword mentioned")

