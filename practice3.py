from googletrans import Translator

t = Translator()
sentence = input("책을 읽으며 인상 깊었던 구절을 적어주세요: ")
# sentence = input("번역을 원하는 문장을 입력하세요 : ")
result1 = t.translate(sentence, dest="en")
result2 = t.translate(sentence, dest="de")
detect = t.detect(sentence)

print("\n============= 번역 결과 ============\n")
print("입력어-", detect.lang, ":", sentence)
print("번역어1-", result1.dest, ":", result1.text)
print("번역어2-", result2.dest, ":", result2.text)
print("\n====================================\n")