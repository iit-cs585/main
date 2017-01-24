# To preprocess Trump's tweets.
import fileinput
import re

if __name__ == '__main__':
  for line in fileinput.input():
      line = re.sub('http\S+', ' ', line)
      print ('<s> %s </s>' % ' '.join(x for x in re.findall('\w+', line.lower())))
