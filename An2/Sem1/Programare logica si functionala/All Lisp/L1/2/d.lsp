(defun elimina (lista elem)
  (cond
    ((null lista) nil)
    ((= (car lista) elem) (elimina (cdr lista) elem))
    (T(cons (car lista) (elimina (cdr lista) elem)))
  )
)

(defun main(lista)
  (cond
    ((null lista) nil)
    (T(cons (car lista) (main (elimina lista (car lista)))))
  )
)
