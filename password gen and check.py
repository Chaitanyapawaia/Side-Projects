from password_generator import digit6_alphanumericcode_generator
from password_generator import digit6_alphanumericcode_checker
print('To login to your account please verify')
originalcode = digit6_alphanumericcode_generator.gen6digitcode()
code= input('Enter the above code:')
digit6_alphanumericcode_checker.check6digitcode(code, originalcode)