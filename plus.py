def plus(num):
    file_object = open('data/'+'DANGLING_PAGE_PR','r')
    try:
    	file_object_writed = open('output/'+str(num)+'.txt', 'a')
        all_the_text = file_object.readlines()
        for x in xrange(0, len(all_the_text)):
            # print all_the_text[x]
            line = long(all_the_text[x]) + num
            file_object_writed.write(str(line)+'\n')
        
        file_object_writed.close()
        file_object.close()
    finally:
        file_object_writed.close()

plus(3333333.0)