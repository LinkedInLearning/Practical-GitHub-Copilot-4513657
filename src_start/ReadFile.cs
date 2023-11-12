using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SampleConsoleApp
{
    public class ReadFile
    {
        public string ReadFileFromPath(string filepath)
        {
            StreamReader sr = new StreamReader(filepath);
            return sr.ReadToEnd();
        }
    }

}
