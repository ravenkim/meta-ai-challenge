import re
import sys

path = sys.argv[1]
lines = open(path, encoding="utf-8").read().split("\n")
body = [l for l in lines if not l.startswith("# ") and not l.startswith("> ")]
with_headers = "\n".join(body).strip()
without_headers = "\n".join(l for l in body if not l.startswith("## ")).strip()


def count(s):
    return len(s), len(re.sub(r"\s", "", s))


print("헤더 포함  공백포함 %d / 공백제외 %d" % count(with_headers))
print("헤더 제외  공백포함 %d / 공백제외 %d" % count(without_headers))

marks = [i for i, l in enumerate(body) if l.startswith("## ")] + [len(body)]
for n in range(len(marks) - 1):
    chunk = "\n".join(body[marks[n] + 1 : marks[n + 1]]).strip()
    print("  씬%d 공백포함 %d" % (n + 1, len(chunk)))
