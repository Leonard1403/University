;postordine(stanga dreapta radacinva)
;v2 
(defun postordine(lista)
  (cond 
    ((null lista) nil)
    (T(append (postordine (cadr lista)) (postordine (caddr lista))  (list (car lista)) ))
  )
)
