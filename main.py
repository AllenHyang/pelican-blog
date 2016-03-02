#!/usr/bin python
#coding=utf-8


import os,sys,subprocess

argv=sys.argv;
base_dir=os.path.dirname(os.getcwd());
def push_blog(cc,comment):
	 
	subprocess.call(["git","add","."],cwd=cc)
	subprocess.call(["git","commit","-m",comment],cwd=cc)
	subprocess.call(["git","push","origin","master"],cwd=cc)

if len(argv)==1:
	print "Pulling from github"
	subprocess.call(["git","pull","origin","master"],cwd=base_dir+"/pelican-blog")
	
	subprocess.call(["git","pull","origin","master"],cwd=base_dir+"/allenhyang.github.io")
else:
	try:
		if argv[1]=="push" and argv[2]=="-m" and argv[3]:
			print "Start to push to github"
			print "Comments:"+argv[3]
			push_blog(base_dir+"/pelican-blog",argv[3])
			push_blog(base_dir+"/allenhyang.github.io",argv[3])			

		else:
			print "Wrong input"
	except:
		print "Wrong input"
