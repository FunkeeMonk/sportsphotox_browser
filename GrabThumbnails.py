#!/usr/bin/python
import sys, web, urllib, string, os
from BeautifulSoup import BeautifulSoup

startingURL = None

def main(argv):
	startingURL = argv[0]
	numberOfPictures = int(argv[1])
	currentStartingIndex = 0

	while currentStartingIndex < numberOfPictures:
		print "Fetching %d" % currentStartingIndex
		s = web.get(startingURL + str(currentStartingIndex))
		#s = open('sample_sportsphotox.txt')
		soup = BeautifulSoup(s)
	
		picContainers = soup.findAll("span", "piccontainer")

		for container in picContainers:
			imgSrc = container.img.attrs[2][1]
			imgFileName = imgSrc[imgSrc.rindex('/') + 1:]

			imgFile = open('thumbs2/' + imgFileName, 'w')
			imgFile.write(web.get(imgSrc))
			imgFile.close()
		
		currentStartingIndex += 10

if __name__ == "__main__":
    main(sys.argv[1:])