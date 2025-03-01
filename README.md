# is601mid

## Summary
This project processes order data from a JSON file to generate two outputs: customers.json, which stores unique customer names and formatted phone numbers, and items.
json, which records item names, prices, and the quantity ordered. 
The structured data helps improve customer management, track item popularity, and provide insights for better decision-making and operational efficiency.

## Features
A JSON file's orders are read.

makes certain that phone numbers are formatted correctly and retrieves client data, such as name and number.

Ordered items, prices, and order frequency are extracted.

employs logging and warnings to resolve issues politely.

separate JSON files with well-structured item and customer data.

File Organization

## Installation

Make sure Python (version 3.6 or above) is installed.and also install vs code/ python Ide
Next, create a clone of the repository


## Algorithm to run the code
Set up Python
Make sure Python 3.6 or later is installed on your computer. To find out what version of Python you are using, run:
Use the following command to run the script:
ui.py orders.json in Python
Check the Output Documents
Two JSON files will be produced in the same directory once the script has been successfully executed:

customers.json (which includes formatted phone numbers and customer names)
item data, such as names, pricing, and order counts, are contained in items.json.

## Check for Errors or Warnings
If the script encounters missing or incorrect data, it will log warnings and errors in the console. Review the messages and ensure the input data is properly formatted.

## Modify and Re-run if Needed
If you need to update the orders or fix errors, modify orders.json and re-run the script using the same command

## Result

Following a successful script execution, the following output files are produced:
A list of distinct customers together with their formatted phone numbers may be found in the customers.json file.
Details about the ordered items, such as the price and order number, are contained in items.json.
These files facilitate effective tracking of frequently ordered commodities and consumer data analysis.