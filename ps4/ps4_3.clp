
(deffacts constants
(w 9.0)
(x 5.0)
(y 32.0))

(defrule mult
   (and (c ?x) (w ?y))
=>
   ; comment
   (assert (u (* ?x ?y))))


(defrule div
   (and (u ?x) (x ?y))
=>
   ; comment
   (assert (v (/ ?x ?y))))


(defrule sum
    (and (v ?x) (y ?y))
=>
    ;comment
    (assert (f (+ ?x ?y))))

(defrule print
(f  ?far)
=>
(printout t ?far crlf))
