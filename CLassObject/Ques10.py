class PrimeNumbers:
    @staticmethod
    def generate_primes(start, end):
        primes = []
        for num in range(start, end + 1):
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    primes.append(num)
        return primes

    @staticmethod
    def calculate_avg(prime_list):
        if not prime_list:
            return 0
        return sum(prime_list) / len(prime_list)


class PalindromeNumbers:
    @staticmethod
    def check_palindrome(numbers):
        palindromes = []
        for num in numbers:
            if str(num) == str(num)[::-1]:
                palindromes.append(num)
        return palindromes


class NumberProcessor(PrimeNumbers, PalindromeNumbers):
    def __init__(self, start, end):
        self.prime_list = self.generate_primes(start, end)
        self.avg_prime = self.calculate_avg(self.prime_list)
        self.palindrome_list = self.check_palindrome(self.prime_list)
        self.num_primes = len(self.prime_list)
        self.num_palindromes = len(self.palindrome_list)

    def display_results(self):
        print("Prime Numbers:", self.prime_list)
        print("Average of Prime Numbers:", self.avg_prime)
        print("Palindrome Numbers:", self.palindrome_list)
        print("Number of Prime Numbers:", self.num_primes)
        print("Number of Palindrome Numbers:", self.num_palindromes)


# Main program
if __name__ == "__main__":
    start = 10
    end = 50
    processor = NumberProcessor(start, end)
    processor.display_results()
