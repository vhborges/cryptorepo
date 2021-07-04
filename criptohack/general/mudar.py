f = open ("flag_7ae18c704272532658c10b5faad06d74.png", "rb")
f1 = open ("flag.png", "wb")

f1.write (f.read()[2:])
