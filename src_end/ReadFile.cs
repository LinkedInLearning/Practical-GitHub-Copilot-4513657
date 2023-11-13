using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SampleConsoleApp
{
    public class ReadFile
    {
        /// <summary>
        /// 指定されたパスからファイルを読み込み、その内容を文字列として返します。
        /// </summary>
        /// <param name="filepath">読み込むファイルのパス</param>
        /// <returns>ファイルの内容を表す文字列</returns>
        public string ReadFileFromPath(string filepath)
        {
            StreamReader sr = new StreamReader(filepath);
            return sr.ReadToEnd();
        }
    }

}
