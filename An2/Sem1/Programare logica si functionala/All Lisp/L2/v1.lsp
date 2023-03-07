;(inordine(stanga radacina dreapta)
(defun inordine(lista)
  (cond
    ((null lista) nil)
    ( T(append (inordine(cadr lista)) (list (car lista)) (inordine(caddr lista))) )
  )
)
