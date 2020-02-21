static/utility-theory-error.png:
	wget https://github.com/glandfried/prospect-theory/releases/download/v.0.0.0/utility-theory-error.png -O static/utility-theory-error.png

bib:
	cd biblio/
	make down f=barberis2013-reviewProspectTheory -C biblio/
	cd ..
	ln -s biblio/download/barberis2013-reviewProspectTheory barberis2013-reviewProspectTheory


