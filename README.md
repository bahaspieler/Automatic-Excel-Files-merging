#Automatic merging of Excel Files
Sometimes there are multiple excel files with same type of data, data-column & so on. In this case, if you need to find a specific
information from these files, you will look into every files. What if all the files would be merged into one
file? But merging so many files into one file is not a easy task. Sometimes the data get mismatched,
sometimes you forget to take some of them and many more. 

So here is a simple python script to merge multiple excel files of same column header. Why same column header? 
Because if the header names aren't same, it will merge the excel files but the columns will not be aligned perfectly.

#Installing Dependencies
In the command window execute the following commands. Make sure of that path of **_pip_** is added to system environment variable.
 
 ` pip install pandas`
 
 `pip install glob3`
 
#Running the script

Clone the repository or dowload it a as a zip file. Open the cmd/terminal on the directory 
that contains the `excel_merging.py` file and execute `python excel_merging.py`. See the output
in the folder `excel files`.