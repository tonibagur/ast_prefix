from ast_model.models import ASTNode
import ast
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def process_structure(n,parent,name,order):
	lineno=None
	col_offset=None
	try:
		lineno=n.lineno
	except:
		pass
	try:
		col_offset=n.col_offset
	except:
		pass
	if type(n)==list:
		child=ASTNode.objects.create(name=name,order=order,type_str='list',content='',parent=parent,line_start=lineno,col_start=col_offset)
		for i,e in enumerate(n):
			process_structure(e,child,i,i)
		return
	else:
		#print "Not iterable"
		pass
	try:
		fields=n._fields
		child=ASTNode.objects.create(name=name,order=order,type_str=str(type(n)),content='',parent=parent,line_start=lineno,col_start=col_offset)
		for i,f in enumerate(fields):
			if f!='col_offset' and f!='lineno':
				process_structure(getattr(n,f),child,f,i)
		return
	except:
		pass
		#import traceback
		#traceback.print_exc()
		#print "Not fields"
	try:
		child=ASTNode.objects.create(name=name,order=order,type_str=str(type(n)),content=str(n),parent=parent,line_start=lineno,col_start=col_offset)
		return
	except:
		pass
		#import traceback
		#traceback.print_exc()
	pass

def scan_file(file_name,parent=None):	
	f=open(file_name,'r')
	content=f.read()
	parent = ASTNode.objects.create(name=file_name,order=1,type_str='FILE',content='',parent=parent)
	n=ast.parse(content)
	process_structure(n,parent,'top',0)

def scan_dir(dir_name):
	import os
	for root,dirs,files in os.walk(dir_name):
		for f in files:
			if f[-3:]=='.py':
				fname=root+'/'+f
				print "Processing:",fname
				scan_file(fname)



def main():
	scan_dir("/Users/toni/dev/migration_phonegap")
	#scan_file("/Users/toni/dev/migration_phonegap/openerp/irvia_interv_prevent/irvia_interv_prevent.py")

