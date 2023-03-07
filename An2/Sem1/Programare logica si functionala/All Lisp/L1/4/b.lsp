(defun lista-atomi(lista)
  (cond
    ((null lista) nil)
    ((atom (car lista))(append (list(car lista))(lista-atomi(cdr lista)) ) )
    (T(append(lista-atomi(car lista))(lista-atomi(cdr lista))))
  )
)
