all: clean
	xelatex HongLouMeng.tex
	xelatex HongLouMeng.tex 
	evince HongLouMeng.pdf &

clean:
	rm -rf HongLouMeng.aux HongLouMeng.idx HongLouMeng.log HongLouMeng.pdf HongLouMeng.toc HongLouMeng.out HongLouMeng.snm HongLouMeng.nav HongLouMeng.vrb

