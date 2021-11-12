\ProvidesClass{RFFE_LETTER}[2016/06/23 RFFE LETTER LaTeX Class v1.0] % Class information printed in the log during every compilation
\usepackage{ifthen} 
\usepackage{lmodern}
\usepackage{blindtext}
\usepackage{lastpage}
%\usepackage{mathptmx} %use font new Times roman
%----------------------or use Arial-------------------------- 
%\renewcommand{\familydefault}{\sfdefault}
%\usepackage{mathptmx}
%-------------------------------------------------------------
\DeclareOption{de}{
	\newcommand{\classtoggle}{de}
}

\DeclareOption{en}{ 
	\newcommand{\classtoggle}{en}
}

\ProcessOptions\relax % Process class options

\LoadClass[a4paper,fontsize=11pt,
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
%-------------------------all koma variables-----------------------------------
\newkomavar{AngebotsNr}
\newkomavar{AngDatum}
\usepackage{fontspec}
\setmainfont{Calibri}
\usepackage{lastpage}
\usepackage{graphicx}
\usepackage{multicol}
\usepackage{tikz}
% ersetze "encoding" durch (im Editor nachschauen, im Zeifelsfall ausprobieren):
% latin1 = oftmals Standard
% utf8 = bei manchen Linux/Unix
% ansinew = Windows
% applemac = Macintosh 
%-----------------------------------------------------------------
\@ifundefined{classtoggle} 
{\ClassError{RFFE_LETTER}{Bitte Sprache wählen}} % If one of the options has not been specified, quit with an error to that effect
{} % Otherwise do nothing

\ifthenelse{\equal{\classtoggle}{de}}
{
	\usepackage[ngerman]{babel}
} % Define the margins as 1 inch on all sides
{} % Otherwise do nothing

\usetikzlibrary{calc}
\setlength{\parindent}{0pt}
%\renewcommand{\familydefault}{\sfdefault}
%\renewcommand*\rmdefault{phv}


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


\renewcommand*{\raggedsignature}{\raggedright}
%\ihead{Seite \pagemark von \pageref{LastPage}}

\@setplength{toaddrhpos}{%
	\dimexpr 1in +\oddsidemargin\relax}


\pagestyle{myheadings}
\setkomavar{nextfoot}[RFFElogo]{
	\hfill
	\vspace*{0.5cm} \includegraphics[scale=0.2]{400dpiLogo.jpg}
}
\@setplength{firstheadvpos}{30mm}%
\setkomavar{nexthead}{
	\vspace*{-2mm}
	\scalebox{1}{\parbox{2\linewidth}{\normalfont{Seite \thepage\ von \pageref{LastPage} der Leistungsbeschreibung \usekomavar{AngebotsNr} vom \usekomavar{AngDatum}}}}}
\endinput