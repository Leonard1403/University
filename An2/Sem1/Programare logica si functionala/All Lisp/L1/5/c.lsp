(defun invers(lista aux)
  (cond
    ((null lista) aux)
    (T(invers (cdr lista) (append (list (car lista)) aux) ))
  )
)

(defun suma(lista1 lista2 retine rezultat)
  (cond
    ((and (> (+ (car lista1) (car lista2)) 9) (= retine 0))
    	suma (cdr lista1) (cdr lista2) 1 (
    )
  )
)
