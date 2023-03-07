(defun select_n (lista n)
  (cond
    ((= n 1)(car lista))
    ((null lista) nil)
    (T(select_n (cdr lista) (- n 1)))
  )
)
