with open(r"C:\Machine-learning-with-python-intership\Week-1\file_handling\poem.txt", "r") as f:
    content = f.read()

if "twinkle" in content.lower():
    print("The poem is about twinkle")
else:
    print("The poem is not about twinkle")