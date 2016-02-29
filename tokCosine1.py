def read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token

def cosine(f1,f2):
	result=0
	mul=1
	with open(f1,'r') as f1_new:
		with open(f2,'r') as f2_new:
		#f1_new = open('%s.txt' % f1, 'r')
		#f2_new = open('%s.txt' % f2, 'r')
			for token1 in read_by_tokens(f1_new):
				words1 = token1.split(token1,":")
				for token2 in read_by_tokens(f2_new):
					words2=token2.split(split2,":")
					if words1[0]==words2[0]:
						mul=float(words1[1])*float(words2[1])
						result=result+mul
			
	return result
	return 1	

f1 = open("first.txt","w")
f2 = open("second.txt","w")
output = open("cosine.txt","w")
c=0
flag=0
with open('output.txt', 'r') as text_file:
	for token in read_by_tokens(text_file):
		if '[' in token:
			flag=1
			output.write(t1)
			token=token[1:]
		if ']' in token:
			c=c+1
			flag=0
			if c==1:
				output.write(",")
			if c==2:
				#sim_val=cosine(f1,f2)
				f1.close()
				f2.close()
				result=0
				mul=1
				with open("first.txt",'r') as f1_new:
					with open("second.txt",'r') as f2_new:
					#f1_new = open('%s.txt' % f1, 'r')
					#f2_new = open('%s.txt' % f2, 'r')
						for token1 in read_by_tokens(f1_new):
							words1 = token1.split(":")
							for token2 in read_by_tokens(f2_new):
								words2=token2.split(":")
								if words1[0]==words2[0]:
									mul=words1[1]*words2[1]
									result=result+mul
									print result
				output.write(":")
				output.write(str(result))
				output.write("\n")
				#f1 = open("first.txt","w")
				#f2 = open("second.txt","w")
				c==0
		if flag is 1:
			if c==0:
				f1.write(token)
				f1.write(" ")
			if c==1:
				f2.write(token)
				f2.write(" ")
		if flag is 0:
			t1=token

