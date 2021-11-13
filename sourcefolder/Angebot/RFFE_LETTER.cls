\ProvidesClass{RFFE_LETTER}[2016/06/23 RFFE LETTER LaTeX Class v1.0] % Class information printed in the log during every compilation
\usepackage{ifthen} 
\usepackage{lmodern}
\usepackage{blindtext}
\usepackage{setspace}
\usepackage{lastpage}
\usepackage{xstring}
%-------------------------------------------------------------
\DeclareOption{de}{
	\newcommand{\classtoggle}{de}
}

\DeclareOption{en}{ 
	\newcommand{\classtoggle}{en}
}

\ProcessOptions\relax % Process class options

\LoadClass[a4paper,
			fontsize=12pt,
			foldmarks=on,
			backaddress=on,
			fromlogo=on,
			fromalign=right,
			fromphone,
			fromfax,
			fromurl,
			fromemail,
			refline=wide,
			subject = titled,
			firstfoot=on,
			refline=fromadressleft,
			%fromalign=locationright
pagenumber=topleft]{scrlttr2} % Load the primary class with set options
\usepackage[top=2.0cm, bottom=2.5cm, left=1in, right=2.0cm]{geometry}
%%%
\LoadLetterOption{visualize}
%-------------------------all koma variables-----------------------------------
\newkomavar{AngebotsNr}
\newkomavar{AngDatum}
\setkomavar{firsthead}
{
	\vspace*{0.8cm}\\
	\includegraphics*[width=0.5\textwidth]{400dpiLogo.jpg}		
	
	\raggedleft\parbox{0.2\textwidth}
	{% Move the \parbox to the right margin and limit its width to the content
		\raggedright
		\vspace*{-2cm}
		{ \footnotesize
			\hspace*{-2cm}
			\begin{tabular*}{\linewidth}{l}
				\usekomavar{fromaddress}
			\end{tabular*}\\
			\hspace*{-2cm}
			\begin{tabular*}{\linewidth}{ll}
				Tel.:& \usekomavar{fromphone}\\
				Fax:& \usekomavar{fromfax}\\
				Email:& \usekomavar{fromemail}\\
				Web:& \usekomavar{fromurl}
			\end{tabular*}
			
			\vspace*{3.5cm}
			{	\normalsize
				\hspace*{-1.9cm}
				\begin{tabular*}{\linewidth}{l}
					\usekomavar{AngebotsNr} \\
					\usekomavar{AngDatum}
				\end{tabular*}
			}
		% forced positioning for the left alignment with the address
		% There should be a smarter way
		}
	}
}
%%%
\usepackage{fontspec}
\setmainfont{Calibri}
\setsansfont[Scale=MatchLowercase]{Calibri}
%\usepackage[utf8]{inputenc}
% ersetze "encoding" durch (im Editor nachschauen, im Zeifelsfall ausprobieren):
% latin1 = oftmals Standard
% utf8 = bei manchen Linux/Unix
% ansinew = Windows
% applemac = Macintosh 

\@ifundefined{classtoggle} 
{\ClassError{RFFE_LETTER}{Bitte Sprache wählen}} % If one of the options has not been specified, quit with an error to that effect
{} % Otherwise do nothing

\ifthenelse{\equal{\classtoggle}{de}}
{
	\usepackage[german]{babel}
} % Define the margins as 1 inch on all sides
{} % Otherwise do nothing

\usepackage[T1,EU1]{fontenc}
\usepackage{lastpage}
\usepackage{graphicx}
\usepackage{multicol}
\usepackage{tikz}
\usetikzlibrary{calc}
\setlength{\parindent}{0pt}
%\renewcommand{\familydefault}{\sfdefault}
%\renewcommand*\rmdefault{phv}
\usepackage{fontspec}
\setmainfont{Calibri}

% RFFE Streifen in grün linke Seite:
\usepackage{background}
\backgroundsetup{opacity=1}
\usepackage{xcolor}
\definecolor{RFFE_green}{RGB}{155,187,89}
\SetBgScale{1}
\SetBgAngle{0}

\SetBgColor{RFFE_green}
\SetBgContents{\rule{0.62cm}{27.6cm}}
\SetBgHshift{-9.5cm}


\setkomavar{backaddress}{RF-Frontend GmbH, Südstr. 8, 47475 Kamp-Lintfort}
\setkomavar{fromaddress}{\textbf{RF-Frontend GmbH}\\
	Südstr. 8\\
	47475 Kamp-Lintfort
}

\setkomavar{fromphone}{02842 / 12360-00}
\setkomavar{phoneseparator}[Tel.]{:~}
\setkomavar{fromfax}{02842 / 9294586}
\setkomavar{fromemail}{info@rf-frontend.de}
\setkomavar{emailseparator}[Email]{:~}
\setkomavar{fromurl}{www.rf-frontend.de}
\setkomavar{urlseparator}[Web]{:~}
\setkomavar{signature}{RF-Frontend GmbH\\\usekomavar{fromname}}
\setkomavar{fromlogo}{\includegraphics[scale=0.4]{400dpiLogo.jpg}}
\setkomavar{date}{}
\renewcommand*{\raggedsignature}{\raggedright}
%\ihead{Seite \pagemark von \pageref{LastPage}}
\@setplength{firstfootvpos}{270mm}
\setkomavar{firstfoot}{
\begin{scriptsize}
\rule{\textwidth}{.4pt}
\vspace*{-2em}
\begin{flushleft}
\begin{multicols}{2}
\hspace*{0.5cm}RF-Frontend GmbH, Südstr. 8, 47475 Kamp-Lintfort\\
\hspace*{0.5cm}Geschäftsführer: Peter Hildenhagen, Dr. Matthias Rittweger\\
\hspace*{0.5cm}AmtsG Kleve: HRB 13080, USt.-IdNr.: DE 815520970\\

\hspace*{0.5cm}Tel.: +49 2842 12360-00, Fax: +49 2842 9294586\\
\hspace*{0.5cm}Email:  info@RF-Frontend.de, Web: www.RF-Frontend.de\\
\hspace*{0.5cm}IBAN DE09 3505 0000 0200 2731 75, BIC DUISDE33XXX
\end{multicols}
\end{flushleft}
\end{scriptsize}

}
\pagestyle{myheadings}
\@setplength{toaddrhpos}{%
	\dimexpr 1in +\oddsidemargin\relax}


\pagestyle{myheadings}
\setkomavar{nextfoot}[RFFElogo]{
	\hfill
	\vspace*{0.5cm} \includegraphics[scale=0.2]{400dpiLogo.jpg}
}
\setkomavar{nexthead}{\vspace*{-2mm}\parbox{2\linewidth}{\normalfont{Seite \thepage\ von \pageref{LastPage} des Angebots \usekomavar{AngebotsNr} vom \usekomavar{AngDatum}}}}
%\KOMAoptions{foldmarks=off}
\endinput