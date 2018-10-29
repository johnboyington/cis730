(defrule is-it-a-duck
(animal-has  webbed-feet)
(animal-has  feathers)
=>
(assert (animal-is  duck)))


(defrule duck
(animal-is  duck)
=>
(assert (sound-is  quack))
(printout t "It is a duck!" crlf))

(deffacts animal-properties
          (animal-has webbed-feet)
          (animal-has feathers))
