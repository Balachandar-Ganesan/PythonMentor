def fnSpeakNow(volume):
    def fnLoud(text):
        return(text.lower())
    def fnLouder(text):
        return (text.upper())
    if volume >0.5:
            return fnLouder
    else:    
            return fnLoud

callFn=fnSpeakNow(0.6)
print(callFn("How are you"))