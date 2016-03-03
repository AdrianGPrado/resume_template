
OUTDIR = pdf

all:
	python generateTemplate.py
	pdflatex resumeAdrianGarcia
	pdflatex coverLetterAdrianGarcia
	mv *.pdf ${OUTDIR}

resume:
	python generateTemplate.py
	pdflatex resumeAdrianGarcia
	mv *.pdf ${OUTDIR}

cover:
	python generateTemplate.py
	pdflatex coverLetterAdrianGarcia
	mv *.pdf ${OUTDIR}

% : %.tex
	pdflatex $@
	mv *.pdf ${OUTDIR}

clean:
	rm -rf *.aux *.log *.toc *.bbl *.blg *.out *.tex *.txt

cleanall: clean
	rm -rf ${OUTDIR}/*.pdf
