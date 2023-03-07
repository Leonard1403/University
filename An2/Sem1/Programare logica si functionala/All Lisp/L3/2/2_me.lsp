
(defun lista_atomi (lista)
  (cond
    ((atom lista) (list lista))
    (T(apply #'append (mapcar #' lista_atomi lista)))
  )
)
