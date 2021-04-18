from hstest.stage_test import *
from hstest.test_case import TestCase
import ast, math

END_RESULT = "No one is going to be lucky"


class BillSplitterTest(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase(stdin=["5", "Marc", "Jem", "Monica", "Anna", "Sam", "100", "Yes"],
                         attach=["5", "100", "Yes", ["Marc", "Jem", "Monica", "Anna", "Sam"]]),
                TestCase(stdin=["0", "100", "No"], attach=["0", "100", "No"]),
                TestCase(stdin=["-1", "-5", "No"], attach=["0", "-5", "No"])
                ]

    def check(self, reply: str, attach: Any) -> CheckResult:
        strings = [s for s in reply.split('\n') if s != '']
        lucky_string = strings[4].split(" ")
        if (len(strings) != 6):
            return CheckResult.wrong(
                "Your code is not printing the expected number of lines in the output, please check the examples.")
        if (attach[2] == "Yes"):
            name = lucky_string[0]
            if (name not in attach[3]):
                return CheckResult.wrong("The expected output is a random name from the dictionary keys.")
        elif (attach[2] == "No"):
            if strings[4] != END_RESULT:
                return CheckResult.wrong("The output should be: No one is going to be lucky.")
        try:
            output = ast.literal_eval(strings[5])
        except ValueError:
            return CheckResult.wrong("Please check your last output, it should be a dictionary.")

        if (not isinstance(output, dict)):
            return CheckResult.wrong("Please check, your last output should be a dictionary.")
        elif (len(output) != int(attach[0])):
            return CheckResult.wrong(
                "Please check if you have added all your friends to the dictionary after taking the user input.")

        if (attach[2] == "Yes"):
            name = lucky_string[0]
            if (len(output) != 0 and output[name] != 0):
                return CheckResult.wrong("The value for the lucky person should be 0!")

        if (len(output) != 0 and math.floor(sum(list(output.values()))) != float(attach[1])):
            return CheckResult.wrong("Please update the dictionary with the correct split values.")
        elif (len(output) != 0 and len(str(math.modf(list(output.values())[0])[0])) > 4):
            return CheckResult.wrong("Please round off the values to two decimal places.")

        return CheckResult.correct()


if __name__ == '__main__':
    BillSplitterTest().run_tests()
