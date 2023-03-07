(defun substituie(lista elem l1)
  (cond
    ((null lista) nil)
    ((listp (car lista)) (cons (substituie (car lista) elem l1)(substituie (cdr lista) elem l1)) )
    ((eq (car lista) elem) (cons l1 (substituie (cdr lista) elem l1)) )
    (T(cons(car lista) (substituie (cdr lista) elem l1)))
  )
)
