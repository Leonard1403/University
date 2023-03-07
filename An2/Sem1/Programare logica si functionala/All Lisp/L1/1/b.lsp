;Definiti o functie care obtine dintr-o lista data lista tuturor atomilor
;care apar, pe orice nivel, dar in ordine inversa. De exemplu: (((A B) C)
;(D E)) --> (E D C B A)
;lista - lista 
(defun obtine(lista)
  (cond
    ;((and (atom (car lista))(equal (cdr lista) nil)) (car lista))
    ((atom lista) (list lista))
    ;((null lista) nil)
    ;((and (atom (car lista))(equal (cdr lista) nil)) (list(car lista) ))
    ((equal (cdr lista) nil) (obtine (car lista)))
    ;(T(append (obtine (car lista)) (obtine (cdr lista)) ))
    (T(append (obtine (cdr lista)) (obtine (car lista))))
  )
)
