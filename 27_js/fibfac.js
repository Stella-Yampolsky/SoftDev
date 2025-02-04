// Team AY: Aditya and Stella
//;; SoftDev pd5
//;; K27 - Basic functions in Scheme
//;; 2025-01-06m
//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

//<your team's fact(n) implementation>
var fact = function(n) {
  if(n==1){
    return 1;
  }
else {
return (n * fact(n-1))}
} 

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
//(fact 1) //"should be 1"
//(fact 5) //should be 120

//-----------------------------------------------------------------


//fib:
var fib = function(n) {
  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  } else {
    return fib(n - 1) + fib(n - 2);
  }
}

//<your team's fib(n) implementation>

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
//(fib 1)
//(fib 5)
//=================================================================
