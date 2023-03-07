(defun elimina(lista elem)
  (cond
    ((null lista) nil)
    ((equal (car lista) elem) (elimina (cdr lista) elem))
    (T(cons (car lista) (elimina (cdr lista) elem)))
  )
)

(defun numara(lista elem)
  (cond
    ((null lista) 0)
    ((equal (car lista) elem)(+ 1 (numara (cdr lista) elem)) )
    (T(numara(cdr lista) elem))
  )
)

(defun main(lista)
  (cond
    ((null lista) nil)
    (T (append(list(append (list(car lista)) (list(numara lista (car lista))))) (main(elimina lista (car lista))) ))
  )
)
