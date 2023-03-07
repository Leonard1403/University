(defun asocieri(lista1 lista2)
  (
   ((null lista1) nil)
   ((null lista2) nil)
   (T(append(list(cons (car lista1)(car lista2))) (asocieri (cdr lista1)(cdr lista2)) ))
  )
)
