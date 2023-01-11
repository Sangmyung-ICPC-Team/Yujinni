import re
#import sys

sen=input()#.strip()

sen=sen[len('<main>'):-len('</main>')]
#print('rr', sen[0], 'ff')
sen=re.sub(r'<div title="([\w ]*)">', r'title : \1\n', sen)
sen=re.sub(r'</div>','',sen)
sen=re.sub(r'<p>','',sen)
sen=re.sub(r'</p>', '\n', sen)
sen=re.sub(r'<[\w ]*>', '', sen)
sen=re.sub(r'</[\w ]*>', '', sen)
sen=re.sub(r'<br >','',sen)
sen=re.sub(r' ?\n ?', '\n', sen)
sen=re.sub(r' {2,}',' ', sen)
sen=sen[:-1]
print(sen)
