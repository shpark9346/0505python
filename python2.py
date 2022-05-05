a = {}

a["이름"] = "박상화"
a["나이"] = "25살"
a["학번"] = "2020161024"
a["학과"] = "시스템생물학과"
a["생일"] = "19980430"

print(a)
print(len(a))
print()

del a["이름"]
del a["나이"]
del a["학번"]
del a["학과"]
del a["생일"]

print(a)
print(len(a))
print()

a = dict(이름 = "박상화", 나이 = "25살", 학번 = "2020161024", 학과 = "시스템생물학과", 생일 = "19980430")

print(a)
print(len(a))
print()

a.clear()
print(a)
print(len(a))
