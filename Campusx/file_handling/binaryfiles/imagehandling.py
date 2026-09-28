def copy_image():
  with open("sample.png", "rb") as f:
    with open("copy_sample.png", "wb") as copy_f:
        copy_f.write(f.read())

copy_image()