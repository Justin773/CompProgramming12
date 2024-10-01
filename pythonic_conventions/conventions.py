import module_name

def main():
    instance_var_name = ClassName("This argument should be a string")
    instance_var_name.method_name('a')

    try:
        module_name.running_this_wont_work()
    except module_name.ExceptionName:
        print("Except this will still work")

# Comments should have a # + a single space and should be capitalised

variable_name = "Double quotes for strings"

CONSTANT_NAME = ("I", "am", "IMMUTABLE")
# Double space for function definitions

def function_name():
    local_variable = "I'll never leave =("
# 2 newlines around class definitions


class ClassName:
    def __init__(self, parameter: str):
        print(parameter)

        # Reserved keywords should have a trailing underscore '_'
        self.class_ = "Mr. Poon's CompProgramming12"

        # Use a leading underscore '_' for non-public properties
        # (i.e private or only accessible from within the class)
        self._for_ClassName_only = (01110000, 01100001, 01110011,
                                    01110011, 01110111, 01101111,
                                    01110010, 01100100)
        # When avoiding text overflow, keep text indentation aligned

    def method_name(self, letter):
        if len(letter) == 1:
            print(f"Chars - '{letter}' - should use single quotes")


if __name__ == "__main__":
    main()

# This exists to ensure the correct file is being run
