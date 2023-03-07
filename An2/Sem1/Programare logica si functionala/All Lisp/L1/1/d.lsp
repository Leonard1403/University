(defun liniar(lista)
  (cond
    ((atom lista) (list lista) )
    ((and (atom (car lista)) (equal (cdr lista) nil)) lista)
    ((equal (cdr lista) nil) (liniar (car lista)))
    (T(append (liniar(car lista)) (liniar(cdr lista))) )
  )
)

(defun aparitii(Lista El)
  (cond
    ((null Lista) 0)
    ((eq (car Lista) El)(+ 1 (aparitii (cdr Lista) El)) )
    (T(aparitii (cdr Lista) El))
  )
)

(defun start(Lista El)
  (aparitii(liniar Lista) El)
)

(defun aparitii2(Lista El)
  (cond
    ((null Lista) 0)
    ((eq (car Lista) El) (+ 1 (aparitii2 (cdr Lista) El)) )
    ((listp (car Lista)) (+ (aparitii2 (car Lista) El) (aparitii2 (cdr Lista) El) ) )
    (T(aparitii2 (cdr Lista) El))
  )
)
