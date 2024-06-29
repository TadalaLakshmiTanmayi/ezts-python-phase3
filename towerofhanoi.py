def TowerOfHanoi(n , source,temp,destination):
	if n==1:
		print (f"move the disk 1 from {source} to {destination}")
		return
	TowerOfHanoi(n-1, source, destination, temp)
	print (f"move the disk {n} from {source} to {destination}")
	TowerOfHanoi(n-1, temp,source,destination)
TowerOfHanoi(3,'s','t','d')