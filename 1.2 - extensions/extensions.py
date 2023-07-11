filename = input("File Name: ").lower().strip()

filetypes = [
    {"end": ".gif", "type": "image/gif"},
    {"end": ".jpg", "type": "image/jpeg"},
    {"end": ".jpeg", "type": "image/jpeg"},
    {"end": ".png", "type": "image/png"},
    {"end": ".pdf", "type": "application/pdf"},
    {"end": ".txt", "type": "text/plain"},
    {"end": ".zip", "type": "application/zip"},
]

for filetype in filetypes:
    if filename.endswith(filetype["end"]):
        print(filetype["type"])
        break
    if filetype == filetypes[-1]:
        print("application/octet-stream")
