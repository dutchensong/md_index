import sys

md_filename = sys.argv[1]

md_file = open(md_filename,"r")


INDEX_1 = '##'
INDEX_2 = '###'
INDEX_3 = '####'

index_1 = 0
index_2 = 0
index_3 = 0

target_file = open(md_filename+"target.md","a")
#print >>target_file, ''

line1 = md_file.readline()

print >>target_file, line1

for line in md_file:
	items = line[:-1].split(' ')
	if items[0] == INDEX_1:
		index_2 = 0
		index_3 = 0
		index_1 = index_1+1
		line_with_enter = line[3:]
		print >>target_file,str(index_1) +' '+line_with_enter[:-1]+'  '
		
	elif items[0] == INDEX_2:
		index_3 = 0
		index_2 = index_2+1
		line_with_enter = line[4:]
		print >>target_file,str(index_1)+'.'+str(index_2)+' '+line_with_enter[:-1]+'  '
	elif items[0] == INDEX_3:
		index_3 = index_3+1
		line_with_enter = line[5:]
		print >>target_file,str(index_1)+'.'+str(index_2)+'.'+str(index_3)+' '+line_with_enter[:-1]+'  '

md_file.close()

md_file = open(md_filename,"r")

for line in md_file:
	print >>target_file,line[:-1]


target_file.close()
md_file.close()