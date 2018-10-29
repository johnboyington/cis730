; Facts:
(deffacts families
(father tom john)    ; tom is father of john
(mother susan john)  ; susan is mother of john
(father george tom)) ; george is father of tom


; Rules:
(defrule parent-rule
(or (father ?x ?y) (mother ?x ?y))
=>
(assert (parent ?x ?y)))


(defrule grandparent-rule
(and (parent ?x ?y) (parent ?y ?z))
=>
(assert (grandparent ?x ?z)))


(defrule grandfather-rule
(and (father ?x ?y) (parent ?y ?z)
)
=>
(assert (grandfather ?x ?z)))
