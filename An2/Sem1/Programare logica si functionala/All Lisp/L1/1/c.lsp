;Definiti o functie care intoarce cel mai mare divizor comun al numerelor
;dintr-o lista neliniara.
;a - atom numeric b - atom numeric
;functia returneaza cmmdc 
(defun cmmdc(a b)
  (cond
    ((< b a)(cmmdc (- a b) b))
    ((< a b)(cmmdc a (- b a)))
    (T a)
  )
)

(defun obtine(lista)
  (cond
    ;((and (atom (car lista))(equal (cdr lista) nil)) (car lista))
    ((atom lista) (list lista))
    ;((null lista) nil)
    ;((and (atom (car lista))(equal (cdr lista) nil)) (list(car lista) ))
    ((equal (cdr lista) nil) (obtine (car lista)))
    ;(T(append (obtine (car lista)) (obtine (cdr lista)) ))
    ;(T(append (obtine (cdr lista)) (obtine (car lista))))
    (T(append (obtine (car lista)) (obtine (cdr lista))))
  )
)

;lista cu atomi numerici

(defun cmmdc_list(lista)
  (cond
    ((and (atom (car lista))(equal (cdr lista) NIL)) (car lista))
    (T(cmmdc_list (append (list (cmmdc (car lista) (cadr lista))) (cddr lista))))
  )
)

(defun start(lista)
  (cond
    (T(cmmdc_list(obtine lista)))
  )
)
