(defun produs(lista1 lista2)
  (cond
    ((and (null lista1) (null lista2)) nil)
    ((null lista1) (cons (car lista2) (produs nil (cdr lista2))) )
    ((null lista2) (cons (car lista1) (produs (cdr lista1) nil)) )
    (T(cons (* (car lista1) (car lista2)) (produs (cdr lista1) (cdr lista2))))
  )
)
