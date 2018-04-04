%Grajeda Barranco Jesús Heber
%Atributes

man(homer).
man(abraham).
man(clancy).
man(mr_burns).
man(skinner).
man(bart).
man(milhouse).

woman(marge).
woman(mona).
woman(jaqueline).
woman(paty).
woman(selma).
woman(lisa).
woman(maggie).
woman(edna).

alien(kang).

cat(snowball).
dog(santas_little_helper).

%Relations

mother(marge, lisa).
mother(marge, maggie).
mother(marge, bart).

mother(jaqueline, marge).
mother(jaqueline, paty).
mother(jaqueline, selma).

mother(mona, homer).

father(abraham, homer).

father(homer, bart).
father(homer, lisa).
father(homer, maggie).

father(kang, maggie).

father(clancy, marge).
father(clancy, paty).
father(clancy, selma).

son(bart, homer).
son(bart, marge).

son(homer, abraham).
son(homer, mona).

daughter(lisa, marge).
daughter(lisa, homer).

daughter(maggie, kang).
daughter(maggie, marge).

daughter(paty, clancy).
daughter(paty, jaqueline).

daughter(selma, jaqueline).
daughter(selma, clancy).

boss(mr_burns, homer).
employee(homer, mr_burns).

pet(snowball, lisa).
pet(santas_little_helper, bart).

friend(bart, milhouse).
slayer(skinner, edna).
%poor skinner :(