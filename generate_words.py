import config as cfg

words = input()

with open(cfg.words_path, "w") as f:
  for word in words.split(" "):
    word += '\n'
    f.write(word.lower())