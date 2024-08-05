# An example of using Selenium WebDriver and Python for test automation
To run the project, follow these steps belows:</br>
<<<<<<< HEAD
1. Install dependencies:</br>
   ```
   pip install -r requirements.txt
   ```
2. Run:
   ```
   pytest (--html=./report/report.html)? (test method)?
=======
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run:
   ```
   pytest (test method)? (--html=./report/report.html)?
>>>>>>> 0a51fd0bb695ed04c3c9854f727888fb3809947d
   ```
   Where:
   <ul>
    <li>
     test method: directory to the test method that you want to test.
     This could be a directory, a method name, or a nodeid (specified -v if using nodeid)
    </li>
    <li>
     --html=./report/report.html: pytest-html argument to generate html report to the folder 'report'
    </li>
   </ul>
