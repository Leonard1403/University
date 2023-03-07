(defun elimina(lista poz n)
  (cond
    ((null lista) nil)
    ((= n poz) (elimina (cdr lista) 1 n))
    (T(append (list (car lista)) (elimina (cdr lista) (+ poz 1) n) ))
  )
)
