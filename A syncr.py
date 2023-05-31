import asyncio
import threading
import random

var1 = 6
var2 = 8
var3 = 11

n1 = 8
n2 = 7
loop_num = 2

# counters for the number of times each process accesses a variable
add1_counter = 0
add2_counter = 0
add3_counter = 0
sub1_counter = 0
sub2_counter = 0
sub3_counter = 0


async def addition():
    global var1, var2, var3, n1, add1_counter, add2_counter, add3_counter
    await asyncio.sleep(1)
    var1 = var1 + n1
    var2 = var2 + n1
    var3 = var3 + n1
    # increment the appropriate counter
    if threading.current_thread().name == 'Thread-1':
        add1_counter += 1
    elif threading.current_thread().name == 'Thread-2':
        add2_counter += 1
    else:
        add3_counter += 1
    print(f"+++ add var1: {var1}")
    print(f"    add var2: {var2}")
    print(f"    add var3: {var3}")
    print()


async def subtraction():
    global var1, var2, var3, n2, sub1_counter, sub2_counter, sub3_counter
    await asyncio.sleep(1)
    var1 = var1 - n2
    var2 = var2 - n2
    var3 = var3 - n2
    # increment the appropriate counter
    if threading.current_thread().name == 'Thread-1':
        sub1_counter += 1
    elif threading.current_thread().name == 'Thread-2':
        sub2_counter += 1
    else:
        sub3_counter += 1
    print(f"--- sub var1: {var1}")
    print(f"    sub var2: {var2}")
    print(f"    sub var3: {var3}")
    print()


async def print_shared_variable_value():
    global var1, var2, var3
    await asyncio.sleep(1)
    print(f"var1: {var1}")
    print(f"var2: {var2}")
    print(f"var3: {var3}")
    print()


async def main_async_add():
    global loop_num
    i = 0
    while i < loop_num:
        i += 1
        await addition()


async def main_async_sub():
    global loop_num
    i = 0
    while i < loop_num:
        i += 1
        await subtraction()


async def shared_variable():
    global loop_num
    i = 0
    while i < loop_num:
        i += 1
        await print_shared_variable_value()


def addf():
    asyncio.run(main_async_add())


def subf():
    asyncio.run(main_async_sub())


def print_result():
    asyncio.run(shared_variable())


thread_add = threading.Thread(target=addf, args=(), name='Thread-1')
thread_add.start()

thread_sub = threading.Thread(target=subf, args=(), name='Thread-2')
thread_sub.start()

thread_shared = threading.Thread(target=print_result, args=(), name='Thread-3')
thread_shared.start()

# wait for all threads to finish
thread_add.join()
thread_sub.join()
thread_shared.join()

# calculate the expected values of the shared variables
expected_var1 = var1 + (add1_counter* n1) - (sub1_counter* n2)
expected_var2 = var2 + (add2_counter * n1) - (sub2_counter * n2)
expected_var3 = var3 + (add3_counter * n1) - (sub3_counter * n2)

# print the expected values of the shared variables
print("Expected value of var1: ", expected_var1)
print("Expected value of var2: ", expected_var2)
print("Expected value of var3: ", expected_var3)

# calculate the actual values of the shared variables
actual_var1 = var1
actual_var2 = var2
actual_var3 = var3

# print the actual values of the shared variables
print("Actual value of var1: ", actual_var1)
print("Actual value of var2: ", actual_var2)
print("Actual value of var3: ", actual_var3)

# check if the actual values match the expected values
if actual_var1 == expected_var1 and actual_var2 == expected_var2 and actual_var3 == expected_var3:
    print("The actual values of the shared variables match the expected values.")
else:
    print("The actual values of the shared variables do not match the expected values.")
