
#include <iostream>
#include <functional>
#include <string>

using std::string;

namespace Functions
{
    class FunctionReciever
    {
        FunctionReciever();
        ~FunctionReciever();
        void FunctionCall(std::function<int(int, int)> function, int num1, int num2);
        void FunctionCall(std::function<string(string)> function, string str);
    };
}