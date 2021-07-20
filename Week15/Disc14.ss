; Scheme

; Write a function that takes a procedure and applies to every element in a given nested list.
(define (deep-map fn lst)
  (cond ((null? lst) lst)
        ((list? (car lst))
          (cons (deep-map fn (car lst)) (deep-map fn (cdr lst))))
        (else (cons (fn (car lst)) (deep-map fn (cdr lst))))
  )
)