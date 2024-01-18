import detection, cutVideo, postVideo, removeOutput


def run():    
    print("Start Highlight Detection")
    detection.run()
    # show.run()
    print("Cut Highlight Video")
    cutVideo.run()
    print("POST to Server")
    # postVideo.run()
    print("Clean Directory")
    # removeOutput.run()