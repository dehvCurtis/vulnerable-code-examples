// The following code is vulnerable to arbitrary code execution 
// because it compiles and runs HTTP data.

using System.CodeDom.Compiler;

public class ExampleController : Controller
{
    public void Run(string message)
    {
        const string code = @"
            using System;
            public class MyClass
            {
                public void MyMethod()
                {
                    Console.WriteLine(""" + message + @""");
                }
            }
        ";

        var provider = CodeDomProvider.CreateProvider("CSharp");
        var compilerParameters = new CompilerParameters { ReferencedAssemblies = { "System.dll", "System.Runtime.dll" } };
        var compilerResults = provider.CompileAssemblyFromSource(compilerParameters, code);
        object myInstance = compilerResults.CompiledAssembly.CreateInstance("MyClass");
        myInstance.GetType().GetMethod("MyMethod").Invoke(myInstance, new object[0]);
    }
}


    // OWASP Top 10 2021 Category A3 - Injection
    // OWASP Top 10 2017 Category A1 - Injection
    // MITRE, CWE-20 - Improper Input Validation
    // MITRE, CWE-95 - Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')
    // SANS Top 25 - Risky Resource Management
