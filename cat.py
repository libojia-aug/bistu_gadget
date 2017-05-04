def cat(lineCount):
    file_object = open('data/'+'2017-03-23-17.log','r')
    try:
        # all_the_text = file_object.read()
        file_object_writed = open('output/'+str(lineCount)+'.txt', 'a')
        for x in xrange(0,lineCount):
            line = file_object.readline()
            file_object_writed.write(line)
        
        file_object_writed.close()
        file_object.close()
    finally:
        file_object_writed.close()

cat(100000)