labelall={"Unknown":"?",
"Closed_Fist":"เวงกำ",
"Open_Palm":"5555",
"Pointing_Up":"ทูบีนัมเบอร์วัน",
"Thumb_Down":"ไม่ชอบอะ",
"Thumb_Up":"ไลค์เลย",
"Victory":"ชนะแน่นอน",
"ILoveYou":"รักนะจุ๊บๆ",
"None":""}
def thlabel(text):
    print(text)
    if labelall[text]:
        return labelall[text]
    else:
        return text
