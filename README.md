# Python-Use-of-Data

Simple personal project using Python to create a system that can make a report about how much data the user had been used in a week.

1. Introduction
The digital era is fully integrated into our society, consequently, the use and consumption of data are increasing more and more. In Brazil, for example, according to G1, 81% of Brazilians, which represents 152 million people, already have internet access and consume more and more mobile data.

Therefore, with the aim of helping users better manage their data usage, the MI Algoritmos class from the State University of Feira de Santana (UEFS) was hired to develop a program that can calculate:
- Total data used by each application per day
- Total data used by each application in a week
- Total overall data used each day
- Total overall data used in a week
- Daily average of total data consumption
- Daily average of data consumption for each application

All of this within a specific one-week period. The MI Algoritmos team managed to develop a functional application that provides freedom and convenience when recording the amount of data used, enabling users to have an idea of their usage over 7 days for better perception and organization.

2. Methodology
In the process of developing this application, the following parameters were considered for its functionality:

Table 1. System Specifications
Development Environment: Vscode
Python Version: 3.10.6
Operating System: Windows 11

To solve this problem, the MI Algoritmos class gathered in groups and discussed different approaches for the functionality of the program, and each student in the class implemented their own code.

During the sessions, it was decided to use accumulator variables to record the information, and I implemented these variables using Python's list function, which facilitated the process of data recording. In the end, there were 6 lists storing values for daily variables and one list for the total daily data of each application. Additionally, there were 5 accumulator variables for the weekly recording of applications and one for the total weekly data.

Through conditional structures for the user-entered data, the application correctly registers the information in the lists according to the chosen day and application. It allows updating a previously entered value, giving the user the freedom to edit the values without worrying about inputting incorrect data. The system also has excellent error handling, eliminating any obstacles on the way to generating the report on the seventh day or upon the user's request.

During the sessions, we also decided to create a menu to facilitate user understanding, providing an overview of the applications that can be used to register data and indicating their codes, as well as the available days.

We also implemented error handling using Try and Except statements to avoid any non-numeric entries for the application codes. It was also discussed whether it would be possible to go back to previous days, and my code allows this freely by simply selecting the desired day; the program automatically updates the values based on the last data entered by the user.

3. Results and Discussions
3.1. Results
In this section, I will detail all the solutions and results, but I decided to divide them into other topics for better understanding.

3.1.1. How to use the program?
When the application is started, the user will see the menu, indicating the parameters for using the application, as shown in the image below:

[Figure 1 - Cyan menu for better visualization]

In the menu, we can already see the set of valid entries for the correct functioning of the program. If the user follows the codes described in the menu, they will not encounter any problems during their usage until the seventh day. However, if the user enters a number not indicated in the menu or writes the name of the application, through the error handling using Try and Except and If and Else statements, the application will print an error message, preventing the user from progressing until they enter a valid value according to the menu.

[Figure 2 - Error message for the application code]

After recording the data, the application will ask the user if they want to continue recording or stop and print the data report by responding "Yes" or "No," accepting any variation of these responses. If the user enters a number or another letter outside of the expected input, the program will stop and only continue when the user enters a valid option according to the text printed on the screen.

When the seventh day is reached, the program will indicate that the report is ready, starting from the first data entered on that day, in a manner similar to "Yes or No," but indicating that it is the last day, and the report is ready for appropriate reading.

3.1.2. How does it work within the program?
In the code, we see more details of how everything mentioned above was implemented. For example, this is the input along with the error handling to prevent unexpected occurrences:

[Figure 3 - Loop for the input of the application code]

In this excerpt of one of the inputs, you can see how it was done. First, a large loop called "While continuar" is established, which is the main loop of the code and only exits when the program asks the user if they want to stop recording data, at which point the variable "Continuar" will be set to "False," breaking the loop.

We can also observe a smaller loop, "While True," in the input, which is only broken if the code value follows the conditions given in the If statement below the input. If not, it will go to the Else part, indicating an incorrect number. If the user enters a letter, the Try statement will identify it and send it to the Except part, printing a red error message and keeping the user in the loop until they enter a valid input. Another example within the code is the conditional part:

[Figure 4 - Conditions for other applications]

In this part, through an Elif statement, the code that the user chooses is appropriately accumulated in the variable and added to the list. We can see that the list is defined with "[dia-1]" to follow the metric desired, as all lists start from 0. It is also noticeable how important the data input is, as it updates all the variables with each loop, always summing the previous values to add to the "total_diario" and "total_semanal" variables.

The definition of colors is also notable for a better understanding of the application. Errors are highlighted in red, the menu in cyan, and, especially, the report stands out since it contains a large amount of printed information. Thus, I formatted it to improve the understanding of the printed content.

3.1.3. How are the outputs printed?
In the output of the application, we have a synthesis of everything that has been worked on so far, a large layer of formatted and colored prints to enhance the user's understanding when reading the data usage report. Each application is displayed in a different color to facilitate identification, as well as the averages and total data, formatted in sections divided by dashes "--------."

3.1.4. Errors and Tests
The main errors were found in conflicting conditionals and, more importantly, in error handling. Hours and hours were spent on verifying "Yes" and "No" at each iteration of the loop. Fortunately, I managed to solve these problems using conditionals and, for numbers, with the use of Try and Except, which is indeed a very useful tool for error checking. In my tests so far, no errors.
