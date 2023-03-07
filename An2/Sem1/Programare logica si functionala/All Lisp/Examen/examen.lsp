(defun nr_niveluri(l)
    (cond
        ((null l) 0)
        ((null (cdr l)) 1)
        (t (+ 1 (max (nr_niveluri (cadr l)) (nr_niveluri (caddr l)))))
    )
)

(defun echilibrat(l)
    (cond
        ((null l) t)
        (t (AND (< (abs (- (nr_niveluri (cadr l)) (nr_niveluri (caddr l)))) 2) (echilibrat (cadr l)) (echilibrat (caddr l))) )
    )
)
