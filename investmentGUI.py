"""
Chapter 9 example (page 249-250)
Program: investmentGUI.py
3/17/2025

**NOTE: the module breezypythongui.py MUST be in the same directory of this file for the app to run properly

GUI- base version of the Investment program from chapter 3
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports can go here

# Class Header (class name will change from project to project)
class TextAreaDemo(EasyFrame):
    
    # Definition of our classes constructor method
    def __init__(self):
        """Comment specific to project"""
        # CALL to the EasyFrame class constructor from breezypythongui.py
        EasyFrame.__init__(self, title = "Investment Calculator 2.0", background= "#D6EFFF")
        # Other components are added here
        self.addLabel(text="Initial Amount", row= 0, column= 0, background= "#D6EFFF")
        self.addLabel(text="Number of Years", row= 1, column= 0, background= "#D6EFFF")
        self.addLabel(text="Interest Rate in %", row= 2, column= 0, background= "#D6EFFF")
        self.amount = self.addFloatField(value= 0.0, row= 0, column= 1, precision= 2)
        self.period = self.addIntegerField(value= 0, row= 1, column= 1)
        self.rate = self.addFloatField(value=0.0, row= 2, column= 1, precision= 2, width= 10)
        self.compute = self.addButton(text= "Calculate", row= 3, column= 0, columnspan= 2, command= self.compute)
        self.outputArea = self.addTextArea(text= "", row= 4, column= 0, columnspan= 2, width= 50, height= 15)

    # Definition of the compute() method which is the event handling method
    def compute(self):
        """Calculates the investment report based on the inputs and outputs to the text area widget using tabular format."""
        # Obtain and validate the inputs
        startBalance = self.amount.getNumber()
        years = self.period.getNumber()
        rate = self.rate.getNumber() / 100
        if startBalance == 0 or years == 0 or rate == 0:
            self.outputArea.setText("NONE OF THE INPUTS SHOULD BE A ZERO")
            return
        # Set the header for the table
        result = "%4s%18s%10s%16s\n" % ("Year", "Starting Balance", "Interest", "Ending Balance")

        # Compute and append the reselts for each year
        totalInterest = 0.0
        for year in range(1, years + 1):
            interest = startBalance * rate
            endBalance = startBalance + interest
            result += "%4d%18.2f%10.2f%16.2f\n" % (year, startBalance, interest, endBalance)
            startBalance = endBalance
            totalInterest += interest
        
        # Append the final totals for the investment period
        result += "Ending Balance: $%0.2f\n" % endBalance
        result += "Total Interest Earned: $%0.2f\n" % totalInterest

        # Output the results variable while keeping read-only status
        self.outputArea["state"] = "normal"
        self.outputArea.setText(result)
        self.outputArea["state"] = "disabled"


# End of class block

# Global definition of the main() function
def main():
    """Instantiate an object from the class into mainloop()"""
    TextAreaDemo().mainloop()

# Global call to main() for program entry
if __name__ == "__main__":
    main()