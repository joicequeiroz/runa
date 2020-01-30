# Runa - QA - Take Home
## Technical Test
### Step 1:
Install:

* Python 3.8.1 (https://www.python.org/downloads/)

### Step 2:
Clone project: 

    * $ git clone git@github.com:joicequeiroz/python.git

### Step 3:
* Execute the commands below:
python -m pip install
pip install -r requeriments.txt
pip install flake8

### Step 4:
In the file environment.py, got to BrowserSetUp method, and chance the path for your preference. This method is responsable to excute browser informed in command line.

### Running automated test cases
#### Run all test cases using Chrome
    <blockquote>$ behave -D browser=chrome</blockquote>

#### Run tests for a specific functionality
Payroll
    <blockquote>$ behave --tags=@payroll -D browser=chrome</blockquote>

### Tecnical approach
This is the first official Python project I have done. I studied Python through courses. However, it is completely different when I have the opportunity to apply that knowledge to a real system.
The system does not have many IDs; for automation tests, it is not a good practice to get elements using XPath because, if the position or something changes on the page, the test will be stopped.
However, my strategy for getting the elements were using Xpath.

It was a great challenge, and I know I still have a lot to learn and develop with that language.
I want to thank you for the opportunity to participate in this process and put my knowledge into practice.

### Suggestions for improvement
1 - In the "Rango de incidencias" field, in the "Nueva Nomina Manual" screen, the field should display the range with the date previously selected in the "Fecha de inicio" field.

### Bugs found
Test Case | Expected Results | Actual Results | Severity
--- | --- | --- | ---
Valid Login | The system should display a password change message. | The system not should display a password change message | Minor