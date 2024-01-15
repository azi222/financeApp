def complain():
    text = input("Введите текст жалобы: ")
    f = open("complains.txt", "a", encoding="utf-8")
    f.write(text+"\n")
    f.close()
    print("Ваша жалоба будет рассмотрена в скором времени.")


def suggestions():
    print("Предложения SkysmartBank")
    f = open("suggestions.txt", "r", encoding="utf-8")
    text = f.read()
    print(text)
    f.close()
