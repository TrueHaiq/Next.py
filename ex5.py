class IDIterator:
    def __init__(self, id=0):
        self._id = id+1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while(self._id <= 999999999):
            id = self._id
            self._id += 1
            if(check_id_valid(id)): return id

        raise StopIteration()
    
def id_gen(id_number):
    id = id_number+1
    while(id<999999999):
        if(check_id_valid(id)): yield id
        id += 1

def check_id_valid(id_number):
    digits = [int(digit) for digit in str(id_number)]

    multiplied_digits = [digits[index] * (index%2+1) for index in range(len(digits))]

    summed_digits = [digit%10 + int(digit/10) for digit in multiplied_digits]
    
    total_sum = sum(summed_digits)

    is_valid = total_sum % 10 == 0
    
    return is_valid

def main():
    id_num = str(input("Enter ID: "))
    input = str(input("Generator or Iterator? (gen/it) ?"))
    if(input == "it"):
        it = IDIterator(id_num)
        for _ in range(10):
            print(next(it))
    elif(input == "gen"):
        gen = id_gen(id_num)
        for id in range(10):
            print(next(gen))

id_num = int(input("Enter ID: "))
input = str(input("Generator or Iterator? (gen/it)? "))
if(input == "it"):
    it = IDIterator(id_num)
    for _ in range(10):
        print(next(it))
elif(input == "gen"):
    gen = id_gen(id_num)
    for id in range(10):
        print(next(gen))
