(defun contine (lista elem)
  (cond
    ((equal (car lista) elem) T)
    ((null lista) nil)
    ((listp (car lista)) (OR (contine (car lista) elem) (contine (cdr lista) elem)) )
    (T(contine (cdr lista) elem))
  )
)
