(define (factorial x) 
  (if (<= x 1) 
  1
  (* x factorial (- x 1)))
)

(define (fib n)
  (if (> n 1)
  (+ (fib (- n 1)) (fib (- n 2))
  n))
)

(define a '(1 2 3))
(eq? a '(1 2 3))   ; #f
(define b a)
(eq? a b)  ; #t  a is b

;; Write a function which takes two lists and concatenates them.
(define (my-append a b)
  (if (null? a)
  b
  (cons (car a) (my-append (cdr a) b))
)

;; Write an expression that selects the value 3 from the list below.
(define s '(5 4 (1 2) 3 7))
(define (sel s)
  (if (eq? 3 (car s))
    3
    (sel (cdr s))
  )
)

;; Write a function that, when given s list, duplicates every element in the list/
(define (duplicate lst)
  (if (null? lst)
    nil
    (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
  )
)

;; Write a function that, when given an element, a list, and an index, inserts the element into the list at that index.
(define (insert element lst index)
  (cond ((= 0 index) (cons element lst))
        ((null? lst) (print 'error))
        (else (cons (car lst) (insert element (cdr lst) (- index 1))))
  )
)

;Q&A

;; multiple x by y (without using the * operator)
;; (mulxy 3 4) -> 12          ; 12 = 3 + 3 + 3 + 3
;; (mulxy (- 3) (- 4)) -> 12  ; 12 = - ( -3 + -3 + -3 + -3 )
(define (mulxy x y)
  (cond ((< y 0) (- (mulxy x (- y))))
        ((= y 0) 0)
        (else (+ x (mulxy x (- y 1))))
  )
)

;; multiple together a list of numbers.
;; (mul '(2 3 4 2)) -> 48
(define (mul s) (reduce mulxy s))

;; evaluate an expression with only calls to * and numbers.
;; (mul-expr '(* (* 1 2) (* 3 (* 4 1 1) 2))) -> 48
(define (mul-expr e)
  (if (number? e) e
    (mul (map mul-expr (cdr e)))
  )
)

;; Convert all calls to * to calls to mul in expression e.
;; (eval (*-to-mul '(* 1 (+ 2 3) (+ 4 5 (* 6 1))))) ->75
;;          (mul (list 1 (+ 2 3) (+ 4 5) (mul (list 6 1))))
(define (*-to-mul e)
  (if (not (list? e)) e
    (let ((op (car e)) (rest (cdr e)))
      (if (equal? op '*)
        (list 'mul (cons 'list (map *-to-mul rest)))
        (cons op rest)
      )
    )
  )
)
