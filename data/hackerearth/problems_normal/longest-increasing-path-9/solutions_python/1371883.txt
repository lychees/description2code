from collections import deque
def adj(matrix,point,n,m):
	points=[]
	x,y,z=point
	if x>=0 and y>=0:
		if x+1<n and matrix[x+1][y]>matrix[x][y]:
			points.append((x+1,y,z+1))
		if y+1<m and matrix[x][y+1]>matrix[x][y]:
			points.append((x,y+1,z+1))
		return points

	return []
def get(matrix,n,m):
	point=(0,0,1)
	visited={}
	q=deque()
	q.appendleft(point)
	me=0
	while len(q)>0:
		top=q.popleft()
		x,y,z=top
		if (x,y) in visited:
			if visited[(x,y)]<z:
				visited[(x,y)]=z
			continue
		visited[(x,y)]=z
		points=adj(matrix,top,n,m)
		for i in points:
			q.appendleft(i)
	return max(visited.values())
tc=int(raw_input())
while tc>0:
	m=1
	tc-=1
	n,m=map(int, raw_input().split())
	matrix=[]
	for i in xrange(n):
		row=map(int, raw_input().split())
		matrix.append(row)
	print get(matrix,n,m)