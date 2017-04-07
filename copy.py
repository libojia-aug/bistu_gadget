def write(count):
    file_object = open('War and Peace.txt')
    try:
        all_the_text = file_object.read()
        file_object = open(str(count)+'.txt', 'w')
        for x in xrange(0,count):
            file_object.write(all_the_text)
        file_object.close()
    finally:
        file_object.close()

#1.txt, 5.txt, 10.txt, 20.txt, 40.txt, 80.txt, 160.txt, 320.txt
write(1)
write(5)
write(10)
write(20)
write(40)
write(80)
write(160)
write(320)