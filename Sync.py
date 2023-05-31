import threading
import time
import random

var1 = 6
var2 = 8
var3 = 11

n1 = random.randint(3, 6)
n2 = random.randint(2, 3)
looping = random.randint(1, 3)

print("n1 = " + str(n1))
print("n2 = " + str(n2))
print("looping = " + str(looping))

add_var1_count = 0
add_var2_count = 0
add_var3_count = 0

sub_var1_count = 0
sub_var2_count = 0
sub_var3_count = 0

threadLock = threading.Lock()

def addition():
    global var1, var2, var3, n1, threadLock, add_var1_count, add_var2_count, add_var3_count
    
    threadLock.acquire()
    time.sleep(1)
    var1 += n1
    var2 += n1
    var3 += n1
    
    add_var1_count += 1
    add_var2_count += 1
    add_var3_count += 1
    
    print("+++add var1: ", var1)
    print("+++add var2: ", var2)
    print("+++add var3: ", var3)
    threadLock.release()

def subtraction():
    global var1, var2, var3, n2, threadLock, sub_var1_count, sub_var2_count, sub_var3_count
    
    threadLock.acquire()
    time.sleep(1)
    var1 -= n2
    var2 -= n2
    var3 -= n2
    
    sub_var1_count += 1
    sub_var2_count += 1
    sub_var3_count += 1
    
    print("---sub var1: ", var1)
    print("---sub var2: ", var2)
    print("---sub var3: ", var3)
    threadLock.release()

def main_add():
    global looping
    i = 0
    while i < looping:
        i += 1
        addition()

def main_sub():
    global looping
    i = 0
    while i < looping:
        i += 1
        subtraction()

def addf():
    main_add()

def subf():
    main_sub()

thread_add = threading.Thread(target=addf, args=())
thread_add.start()

thread_sub = threading.Thread(target=subf, args=())
thread_sub.start()

threads = []
threads.append(thread_add)
threads.append(thread_sub)

for t in threads:
    t.join()

# Calculate the expected values of the shared variables
expected_var1 = 6 + (n1 * looping) - (n2 * looping)
expected_var2 = 8 + (n1 * looping) - (n2 * looping)
expected_var3 = 11 + (n1 * looping) - (n2 * looping)

# Print the expected and actual values of the shared variables
print("Expected values:")
print("var1 = " + str(expected_var1))
print("var2 = " + str(expected_var2))
print("var3 = " + str(expected_var3))

print("Actual values:")
print("var1 = " + str(var1))
print("var2 = " + str(var2))
print("var3 = " + str(var3))

# Calculate the expected number of times each variable was accessed by adders and subtractors
expected_add_var1_count = looping
expected_add_var2_count = looping
expected_add_var3_count = looping

expected_sub_var1_count = looping
expected_sub_var2_count = looping
expected_sub_var3_count = looping

# Compare expected and actual variable counts
print("Expected counts:")
print("Adder var1:", expected_add_var1_count)
print("Adder var2:", expected_add_var2_count)
print("Adder var3:", expected_add_var3_count)
print("Subtractor var1:", expected_sub_var1_count)
print("Subtractor var2:", expected_sub_var2_count)
print("Subtractor var3:", expected_sub_var3_count)

print("\nActual counts:")
print("Adder var1:", add_var1_count)
print("Adder var2:", add_var2_count)
print("Adder var3:", add_var3_count)
print("Subtractor var1:", sub_var1_count)
print("Subtractor var2:", sub_var2_count)
print("Subtractor var3:", sub_var3_count)
