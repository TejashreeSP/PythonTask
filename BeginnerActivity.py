def are_anagrams(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    
    return sorted(str1) == sorted(str2)


s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2))  


from collections import Counter

def most_frequent_element(lst):
    if not lst:
        return None
    counter = Counter(lst)
    most_common = counter.most_common(1)[0]
    return most_common[0], most_common[1]  # (element, frequency)


sample_list = [1, 3, 2, 3, 4, 3, 5, 2, 1]
element, frequency = most_frequent_element(sample_list)
print(f"The most frequent element is {element} (appears {frequency} times).")


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


try:
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
except ValueError:
    print("Please enter a valid integer.")


