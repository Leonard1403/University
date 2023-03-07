(defun depth (lst)
  (cond ((null lst) 0)
        ((not (listp lst)) 0)
        (t (+ 1 (apply #'max (mapcar #'depth lst))))))

