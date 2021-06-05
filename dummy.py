import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Do you suffer from any health diseases?")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        st=format(text)
        #print(st)
        if(st=="I have cancer and thyroid"):
            thislist = ["Cancer", "Thyroid"]
            print(thislist)
        elif(st=="I have no disease"):
            thislist=["None"]
            print(thislist)
        elif(st=="I have Thyroid and High Blood pressure "):
            thislist=["Thyroid","Others"]
            print(thislist)
        elif(st=="I have High Blood pressure "):
            thislist=[]
            print(thislist)
        
    except:
        print("Sorry could not recognize what you said")
r = sr.Recognizer()
with sr.Microphone() as source:
    print("What’s your annual income?")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        st=format(text)
        #print(st)
        if(st=="700000"):
            thislist = ["5lakh-10lakh"]
            print(thislist)
        elif(st=="300000"):
            thislist=["<5lakh"]
            print(thislist)
    except:
        print("Sorry could not recognize what you said")
r = sr.Recognizer()
with sr.Microphone() as source:
    print("What is your dob?")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        st=format(text)
        #print(st)
        if(st=="23rd December 1998"):
            thislist = ["23/12/1998"]
            print(thislist)
        elif(st=="22 10 1998"):
            thislist=["22/12/1998"]
            print(thislist)
        elif(st=="1998 10 22"):
            thislist=["22/10/1998"]
            print(thislist)
    except:
        print("Sorry could not recognize what you said")