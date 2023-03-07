;Sa se insereze intr-o lista liniara un atom a dat dupa al 2-lea, al 4-lea,
;al 6-lea,....element.
;lista - lista pozitie - atom numeric elem - atom numeric
(defun inserare(lista pozitie elem)
	(cond
	   ((and (null lista)(eq (mod pozitie 2) 0)) (list elem))
	   ((null lista) nil)
	   (T(cond
	   	 	((and (/= pozitie 0)(eq (mod pozitie 2) 0)) (cons elem (inserare lista 0 elem) ))
	   	 	(T (cons (car lista) (inserare (cdr lista) (+ pozitie 1) elem) ))
		 )
	   )
	)
)


(defun inser(a l)
 	(cond
  		((atom (cdr l)) l)
  		(T( append (list (car l) (car (cdr l)) a) (inser a (cddr l))))
  	)
)
