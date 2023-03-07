(defun minim(lista)
  (cond
    ((null lista) 1000)
    (T(min (car lista) (minim (cdr lista))))
  )
)

(defun elimina_element(lista elem)
  (cond
    ((null lista) nil)
    ((= (car lista) elem)(elimina_element (cdr lista) elem))
    (T(cons (car lista) (elimina_element (cdr lista) elem)))
  )
)

(defun main(lista)
  (cond
    ((null lista) nil)
    (T(cons (minim lista) (main(elimina_element lista (minim lista) )) ))
  )
)
