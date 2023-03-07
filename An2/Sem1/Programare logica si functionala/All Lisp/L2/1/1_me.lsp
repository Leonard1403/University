;inordine(stanga radacina dreapta)

;(defun inordine(lista)
;  (cond
;    ((eq (cadr lista) 0) -1)
;    (T (inordine(caddr lista)))
;  )
;)

;nv - numar varfuri | nm - numar muchii

(defun parcurg_st(arb nv nm)
  (cond
    ((null arb) nil)
    ((= nv (+ nm 1))  nil)
    (T(cons (car arb)(cons (cadr arb) (parcurg_st (cddr arb) (+ nv 1) (+ nm (cadr arb)))) ))
  )
)

(defun parcurg_dr(arb nv nm)
  (cond 
    ((null arb) nil)
    ((= nv (+ nm 1)) arb)
    (T(parcurg_dr (cddr arb) (+ nv 1) (+ nm (cadr arb))))
  )
)

(defun inordine(lista)
  (cond
    ((null lista) nil)
    (T(append (inordine (parcurg_st (cddr lista) 0 0)) (list (car lista)) (inordine(parcurg_dr (cddr lista) 0 0))))
  )
)

(defun preordine(lista)
  (cond 
    ((null lista) nil)
    (T(append (list (car lista)) (preordine(parcurg_st (cddr lista) 0 0)) (preordine(parcurg_dr (cddr lista) 0 0)) ))
  )
)

(defun postordine(lista)
  (cond
    ((null lista) nil)
    (T(append (inordine (parcurg_st (cddr lista) 0 0)) (inordine(parcurg_dr (cddr lista) 0 0)) (list (car lista)) ))
  )
)

(defun apare(arb c)
  (cond 
    ((null arb) nil)
    ((equal (car arb) c) T)
    (T( apare (cddr arb) c))
  )
)

(defun path(arb x)
  (cond
    ((equal (car arb) x) (list x))
    ((apare(parcurg_st (cddr arb) 0 0) x) (append (list(car arb)) (path(parcurg_st (cddr arb) 0 0) x)) )
    ((apare(parcurg_dr (cddr arb) 0 0) x) (append (list(car arb)) (path(parcurg_dr (cddr arb) 0 0) x)) )
    (T(nil))
  )
)
