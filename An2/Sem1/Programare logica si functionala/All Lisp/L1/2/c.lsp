(defun subliste(lista)
  (cond
    ((null lista) nil)
    ((listp (car lista)) (cons (car lista) (append (subliste(car lista)) (subliste(cdr lista)) )) )
    ((atom (car lista)) (subliste(cdr lista)))
    (T(nil))
  )
)

(defun main(lista)
  (cond
    (T(cons lista (subliste lista) ))
  )
)

(defun sublists (lst)
  (cond 
    ((null lst) nil)
    ((listp (car lst))(cons (car lst) (append (sublists (car lst)) (sublists (cdr lst)))))
    (t (cons lst (sublists (cdr lst))))
  )
)
