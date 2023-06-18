QUESTION:-1. What is multithreading in python? Why is it used? Name the module used to handle threads in python.
Multithreading refers to concurrently executing multiple threads by rapidly switching the control of the CPU between threads.enables efficient utilization of the resources as the threads share the data space and memory.Threading Modules used to handle threads in python. 



QUESTION:-2. Why threading module used? Write the use of the following functions.
1.activeCount()
2.currentThread()
3.enumerate()

Python threading allows you to have different parts of your program run concurrently and can simplify your design.
1. activeCount() :- Returns the number of total python thread that are active.
2. currentThread() :- Return the current Thread object, corresponding to the caller's thread of control.
3. enumerate() :- Return a list of all Thread objects currently active.



QUESTION:-3. Explain the following functions.
1.run()
2.start()
3.join()
4.isAlive()

1. run() :- A function is a block of code which only runs when it is called run function.
2. start() :- Returns an integer that is the position in the text where the match starts.
3. join() :- Join in python is an in-built method used to join an iterable's elements, separated by a string separator, which is specified by you.
4. isAlive() :- It is used to check whether that thread is alive or not, ie, it is still running or not.



QUESTION:-4. Write a python program to create two threads. Thread one must print the list of squares and thread two must print the list of cubes.
import threading
def thread_function_1():
    print("Thread 1 is executing")
def thread_function_2():
    print("Thread 2 is executing")
thread_1 = threading.Thread(target=thread_function_1)
thread_2 = threading.Thread(target=thread_function_2)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
print("Program execution completed.")



import threading
def print_squares():
    squares = [x ** 2 for x in range(1, 11)]
    for square in squares:
        print(square)
def print_cubes():
    cubes = [x ** 3 for x in range(1, 11)]
    for cube in cubes:
        print(cube)
thread_1 = threading.Thread(target=print_squares)
thread_2 = threading.Thread(target=print_cubes)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
print("Program execution completed.")



QUESTION:-5. State advantages and disadvantages of multithreading.
Advantages Of Multithreading :- 
(i). Concurrent Execution: Multithreading allows concurrent execution of multiple threads within a single process. This means that multiple tasks can be executed simultaneously, which can significantly improve the overall speed and responsiveness of your program. For example, you can perform time-consuming computations in one thread while another thread handles user input or updates the user interface.
(ii). Responsiveness: By using multiple threads, your program can remain responsive even while executing long-running or blocking operations. For instance, if you have a graphical user interface (GUI) application, you can offload time-consuming tasks to separate threads, ensuring that the UI remains interactive and doesn't freeze or become unresponsive. 

Disadvantages Of Multithreading :-
(i). Global Interpreter Lock (GIL): Python has a Global Interpreter Lock (GIL) that allows only one thread to execute Python bytecode at a time. This means that even though you have multiple threads, only one thread can be actively executing Python code at any given moment. As a result, multithreading in Python may not fully exploit the potential of multicore processors for CPU-bound tasks.
(ii). Limited CPU-bound Performance Improvement: Due to the GIL, multithreading in Python primarily benefits I/O-bound or latency-bound tasks, where threads can overlap waiting times with useful computations. However, for CPU-bound tasks that do not involve waiting for external resources, multithreading may not provide significant performance improvements, and multiprocessing or other concurrency models might be more suitable.



QUESTION:-6. Explain deadlocks and race conditions.
Deadlocks Condition :- A deadlock is a concurrency failure mode where a thread or threads wait for a condition that never occurs.
Race Condition :- Your program's result might depend on the order of execution of the individual steps.
