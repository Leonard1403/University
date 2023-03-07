;4. Sa se converteasca un arbore de tipul 
;(2) la un arbore de tipul (1).

(defun conversie(Arb)
  (cond
    ((and (equal (cdr Arb) nil) (equal (cddr Arb) nil)) (list (car Arb) 0))
    ((and (listp (cdr Arb)) (equal (cddr Arb) nil)) (append (list (car Arb) 1) (conversie(cadr Arb))))
    (T(append (list (car Arb) 2) (conversie(cadr Arb)) (conversie(caddr Arb))))
  )
)
