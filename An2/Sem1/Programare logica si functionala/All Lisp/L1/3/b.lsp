(defun adancime(lista nivel)
  (cond
    ((null lista) 0)
    ((listp(car lista))(max nivel (adancime (car lista) (+ 1 nivel)) (adancime (cdr lista) nivel)  ))
    (T (max nivel (adancime (cdr lista) nivel) ))
  )
)

(defun depth (lst)
  (cond ((null lst) 0)
        ((not (listp (car lst))) (depth (cdr lst)))
        (t (1+ (max (depth (car lst)) (depth (cdr lst))))))
)
