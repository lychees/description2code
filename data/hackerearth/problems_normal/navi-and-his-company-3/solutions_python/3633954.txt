for _ in xrange(int(raw_input())):
	n=int(raw_input());	ct,val=0,0;
	for i in xrange(n):
		q=raw_input();
		if q[0]=='N':
			if ct<=0:
				val+=1;
			else:
				ct-=1;
		else:
			ct+=int(q);
	print val
