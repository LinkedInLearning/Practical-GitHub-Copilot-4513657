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
            try
            {
                using (StreamReader sr = new StreamReader(filepath))
                {
                    return sr.ReadToEnd();
                }
            }
            catch (Exception e)
            {
                Console.WriteLine($"ファイルの読み込み中にエラーが発生しました: {e.Message}");
                return null;
            }
        }
    }

}
