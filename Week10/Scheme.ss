;Sierpinski's triangle

(define (line) (fd 50))
(define (twice fn) (fn) (fn))

(define (repeat k fn)
    (fn)
    (if (> k 1) (repeat (- k 1) fn)))

(define (tri fn)
    (repeat 3 (lambda () (fn) (lt 120))))

(define (sier d k)
    (tri (lambda () (if (= d 1) (fd k) (leg d k)))))
(define (leg d k)
    (sier (- d 1) (/ k 2))
    (penup) (fd k) (pendown))

(rt 90)
(speed 0)
(sier 5 200)


;Cond

(cond ((> x 10) (print 'big))
      ((> x 5)  (print 'medium))
      (else     (print 'small)))

(print
    (cond ((> x 10) ('big)
        ((> x 5)  ('medium)
        (else     ('small)))

(cond ((> x 10) (begin (print 'big) (print 'guy)))
      (else     (begin (print 'small) (print 'fry))))

(if (> x 10) (begin
                (print 'big)
                (print 'guy))
             (begin
             (print 'small)
             (print 'fry)))


;Let

(define c (let ((a 3)
                (b 4)) ;binding of let expression
               (sqrt (+ (* a a) (* b b))))) ;value of let expression


;Lists

(define s ((cons 1 (cons 2 (cons 3 (cons 4 nil))))))
(1 2 3 4)
(draw s)
(list? s)
(list? nil)
(null? nil)

(list 1 2 3 4)
(cons 0 (cdr (list 1 2 3 4)))


;list can represent combinations

(list 'quotient 10 2)
(eval (list 'quotient 10 2))
(list '+ 1 2)
(list '+ 1 (+ 2 3))

fact (lambda (n) (if (= n 0) 1 (* n (fact (- n 1)))))
(define (fact n) (if (= n 0) 1 (* n (fact (- n 1)))))
(define (fact-exp n) (if (= n 0) 1 (list '* n (fact-exp (- n 1)))))
(define (fib n)
    (if (<= n 1) n (+ (fib (- n 2)) (fib (- n 1)))))
(define (fib-exp n)
    (if (<= n 1) n (list '+ (fib-exp (- n 2)) (fib-exp (- n 1)))))


;Quasiquotation

(define (make-add-procedure n) `(lambda (d) (+ d ,n)))

(begin    ;the sum of the squares of even numbers less than 10 starting with 2
    (define (f x total)
        (if (< x 10)
            (f (+ x 2) (+ total (* x x)))
            total))
(f 2 0))

(begin    ;the sum of the numbers whose squares are less than 50 starting with 1
    (define (f x total)
        (if (< (* x x) 50)
        (f (+ x 1) (+ total x)
        total))
(f 1 0))

; write a program that generates programs
(define (sum-while   initial-x     condition       add-to-total   update-x)
;       (sum-while      1        '(< (* x x) 50)      'x          '(+ x 1))
    `(begin
        (define (f x total)
        (if ,condition
        (f ,update-x (+ total ,add-to-total))
        total))
    (f ,initial-x 0)))
(define result  (sum-while      1        '(< (* x x) 50)      'x        '(+ x 1)))
(list? result)
(car result)
(cdr result)
(eval result)
(eval (sum-while 2 '(< x 10) '(* x x) '(+ x 2))) ;return a program and evaluate it


;Q & A

(define (even? n)  ;() after define means building a procedure
    (zero? (remainder n 2)))
(define (sum-even s)  
   ;  (sum-even '(2 4 6)) => 12
   ;  (sum-even  '(1 2 3 4 5 6) => 12
    (if (null? s)
        0
        (if (even? (car s))
            (+ (car s) (sum-even (cdr s)))
            (sum-even (cdr s)))))

(define foo (lambda (x y z) (if x y z)))
(foo (> 2 1) 5 (print 7)) ;(true, 5, None/undefined)

(define (make-withdraw balance)
    (define (withdraw amount)
        (set! balance (- balance amount)) ;nonlocal balance
        balance)
    withdraw)
