#include "FunctionReciever.h"

namespace Functions
{
    FunctionReciever::FunctionReciever()
    {   
    }
    FunctionReciever::~FunctionReciever()
    {
    }
    void FunctionReciever::FunctionCall(std::function<int(int, int)> function, int num1, int num2)
    {
        function(num1,num2);
    }
    void FunctionReciever::FunctionCall(std::function<string(string)> function, string str)
    {
        function(str);
    }
}