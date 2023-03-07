(defun invers(l aux)
  (cond
    ((null l) aux)
    ((listp (car l))(append aux (append (list (invers(car l) nil))(invers(cdr l) nil))))
    (T(invers(cdr l)(append (list (car l)) aux)))
  )
)
