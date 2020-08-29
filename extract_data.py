import os

file = open('resumes.txt', 'r')

for resume in range(25):
    file_add = open('resume_{}_data.txt'.format(str(resume+1)),'w')
    for i in file:
        if i[:2] == 'ed':
            file_add.write(i[11:])
        if i[:2] == 'me':
            file_add.write(i[6:])
        if i[0] == '+':
            file_add.close()
            break

file.close()